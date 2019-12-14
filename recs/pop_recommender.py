from decimal import Decimal

from recs.base_recommender import base_recommender
from django.db.models import Count, Q, Avg

class pop_recommender(base_recommender):

    @staticmethod
    def recommend_items_from_log(num=6):
        pass

    @staticmethod
    def recommend_items_by_ratings(num=6):
        pass