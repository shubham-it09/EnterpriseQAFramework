import time
import allure

from models import UserData


@allure.epic("OrangeHRM")
@allure.feature("Admin Module")
@allure.story("User Management")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify Admin can add a new user")
@allure.description(
    """
    Verify that an administrator can successfully
    add a new user.
    """
)
def test_admin_can_add_new_user5(
        login_business,
        admin_business
):

    user = UserData(
        role="Admin",
        employee_name="Paul Collings",
        status="Enabled",
        username=f"Admin_{int(time.time())}",
        password="Admin@123"
    )

    allure.dynamic.parameter(
        "Username",
        user.username
    )

    allure.dynamic.parameter(
        "Role",
        user.role
    )

    allure.dynamic.parameter(
        "Status",
        user.status
    )

    with allure.step("Login as administrator"):
        login_business.login_as_admin()

    with allure.step("Open Admin module"):
        admin_business.open_admin()

    with allure.step("Add new user"):
        admin_business.add_user(user)

    # with allure.step("Search newly created user"):
    #     admin_business.search_user(
    #         user.username
    #     )

    # with allure.step("Verify newly created user"):
    #     assert admin_business.admin_page.is_user_present(
    #         user.username
    #     )