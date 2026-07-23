def test_get_all_bookings(
        booking_business
):
    """
    Verify all bookings can be retrieved.
    """

    response = booking_business.get_all_bookings()
    print("\n ***************Response is************** \n  ",response)

    assert response.status_code == 200

def test_get_all_bookings1(
        booking_business
):

    response = booking_business.get_all_bookings()

    assert response.status_code == 200

    bookings = response.json()
    # print("\n ***************Response is************** \n  ",bookings)

    assert isinstance(bookings, list)

    assert len(bookings) > 0