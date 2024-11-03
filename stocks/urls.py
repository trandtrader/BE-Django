from django.urls import path

from stocks.views import FetchAllStocksInfoView, StockSearchView, AddStockToWeeklyView, WeeklyRecommendationStocksView, \
    FetchWeeklyStockDailyDataView, LatestWeeklyStocksDataView, StockAITestView, StockAIPredictView, \
    StockAITestResultView, StockAIPredictResultView

urlpatterns = [

    # admin api urls

    # 주식 검색
    path('', StockSearchView.as_view(), name="stock-search"),

    # 주식 기본 데이터 저장 (처음 해야할 작업)
    path('info/', FetchAllStocksInfoView.as_view(), name="fetch-all-stocks-info"),

    # 주차별 주식 목록 (GET)
    path('weekly/', WeeklyRecommendationStocksView.as_view(), name='weekly_stocks'),

    # 주차별 주식 추가 (POST)
    path('weekly/<int:stock_id>', AddStockToWeeklyView.as_view(), name='add_weekly_stock'),

    # 전체 주식 정보 가져오기 (POST)
    path('weekly/daily-data', FetchWeeklyStockDailyDataView.as_view(), name='stock_info'),

    # 최신 주차별 주식 데이터 test(Post)
    path('weekly/latest/test/', StockAITestView.as_view(), name='latest_weekly_stocks_test'),

    # 최신 주차별 주식 데이터 predict(Post)
    path('weekly/latest/predict/', StockAIPredictView.as_view(), name='latest_weekly_stocks_predict'),



    # 일반 api urls

    # 최신 주차별 주식 데이터 (GET)
    path('weekly/latest/', LatestWeeklyStocksDataView.as_view(), name='latest_weekly_stocks'),

    # 최신 주차별 주식 데이터 test(Get)
    path('weekly/latest/test/<str:isin_code>', StockAITestResultView.as_view(), name='latest_weekly_stocks_test_data'),

    # 최신 주차별 주식 데이터 predict(Get)
    path('weekly/latest/predict/<str:isin_code>', StockAIPredictResultView.as_view(), name='latest_weekly_stocks_predict_data'),
]