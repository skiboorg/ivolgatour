from django.db import models
from tour.models import Tour
from customuser.models import User


class Comment(models.Model):
    commentFrom = models.ForeignKey(User, blank=False, null=True, on_delete=models.CASCADE, verbose_name="Отзыв от", related_name='comment_from')
    commentTour = models.ForeignKey(Tour, blank=False, null=True, on_delete=models.CASCADE, verbose_name="Отзыв к туру", related_name='comment_tour')
    rating = models.IntegerField('Оценка', default=5)
    commentText = models.TextField('Отзыв', blank=False, null=True)
    created_at = models.DateField('Дата', auto_now_add=True)

    def __str__(self):
        return 'Отзыв от {} о туре {} '.format(self.commentFrom.fio,self.commentTour.name)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"