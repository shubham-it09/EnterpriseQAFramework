from ai.analyzers.root_cause_analyzer import RootCauseAnalyzer
from ai.collectors.failure_collector import FailureCollector,FailureContext


def test_root_cause_analyzer():

    context = FailureCollector.collect(

    test_name="test_login",

    error=Exception("TimeoutError"),

    stack_trace="Locator.click() timeout",

    page_url="https://opensource-demo.orangehrmlive.com"

    )

    response = RootCauseAnalyzer.analyze(context)
    # print("\n================ AI RESPONSE ================")
    # print("Success :", response.success)
    # print("Provider:", response.provider)
    # print("Model   :", response.model)
    # print("Tokens  :", response.tokens)
    # print("Error   :", response.error)
    print("----------------Response----------------------------")
    print(response.response)
    print("=============================================\n")

    

    assert response.success

def test_ai_failure(page):

    page.goto("https://opensource-demo.orangehrmlive.com/")

    assert False, "Intentional failure"