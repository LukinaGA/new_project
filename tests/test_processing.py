from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(transaction_info_for_processing):
    assert filter_by_state(transaction_info_for_processing) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    assert filter_by_state(transaction_info_for_processing, "CANCELED") == [
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]


def test_filter_by_state_empty_list():
    assert filter_by_state([]) == []


def test_filter_by_state_without_required_state():
    assert (
        filter_by_state(
            [
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ]
        )
        == []
    )


def test_sort_by_data(transaction_info_for_processing):
    assert sort_by_date(transaction_info_for_processing) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    assert sort_by_date(transaction_info_for_processing, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_empty_list():
    assert sort_by_date([]) == []


def test_sort_by_date_one_transaction():
    assert sort_by_date([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]) == [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        }
    ]
