from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Poll(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return u'poll #%s %s' % (self.id, self.name[:20])


class Question(models.Model):
    poll = models.ForeignKey(Poll)

    question = models.TextField()
    allow_user_answer = models.BooleanField(default=True)

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

    def __unicode__(self):
        return u'poll #%s %s: %s' % (self.poll_id, self.question.question[:20], self.answer[:20])


class UserAnswer(models.Model):
    user = models.ForeignKey('auth.User')
    poll = models.ForeignKey(Poll)
    question = models.ForeignKey(Question)
    answer = models.TextField()

    def __unicode__(self):
        return u'answer (%s): poll #%s %s: %s' % (self.user_id, self.poll_id, self.question.question[:20], self.answer[:20])
