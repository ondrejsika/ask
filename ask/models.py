from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Poll(models.Model):
    name = models.CharField(max_length=128)
    reward = models.IntegerField()

    def __unicode__(self):
        return u'poll #%s %s' % (self.id, self.name[:20])


class Question(models.Model):
    poll = models.ForeignKey(Poll)

    question = models.TextField()
    allow_user_answer = models.BooleanField(default=True)

    class Meta:
        unique_together = ('poll', 'question')

    def __unicode__(self):
        return u'poll #%s %s' % (self.poll_id, self.question[:20])


class Answer(models.Model):
    poll = models.ForeignKey(Poll)
    question = ChainedForeignKey(
        Question,
        chained_field='poll',
        chained_model_field='poll',
        show_all=False,
    )
    answer = models.TextField()

    class Meta:
        unique_together = ('poll', 'question', 'answer')

    def __unicode__(self):
        return u'poll #%s %s: %s' % (self.poll_id, self.question.question[:20], self.answer[:20])


class UserAnswer(models.Model):
    user = models.ForeignKey('auth.User')
    poll = models.ForeignKey(Poll)
    question = models.ForeignKey(Question)
    answer = models.TextField()

    class Meta:
        unique_together = ('user', 'poll', 'question', 'answer')

    def __unicode__(self):
        return u'answer (%s): poll #%s %s: %s' % (self.user_id, self.poll_id, self.question.question[:20], self.answer[:20])


class Payout(models.Model):
    user = models.ForeignKey('auth.User')
    amount = models.IntegerField()
    timestamp_dt = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'payout %s %s %s' % (self.user, self.amount, self.timestamp_dt)


class Profile(models.Model):
    user = models.OneToOneField('auth.User')

    completed_polls = models.ManyToManyField(Poll, blank=True)

    email = models.EmailField(null=True, blank=True)
    bank_account = models.CharField(max_length=32, null=True, blank=True)

    def __unicode__(self):
        return u'profile %s %s (%s)' % (self.user, self.user_id, self.get_balance())

    def get_balance(self):
        sum_rewards = self.completed_polls.all().aggregate(models.Sum('reward'))['reward__sum'] or 0
        sum_payouts = Payout.objects.filter(user=self.user).aggregate(models.Sum('amount'))['amount__sum'] or 0
        return sum_rewards - sum_payouts
