import  pytest



from work_pytest.PageObjects.ketangpai_login_page import LoginPage as lp
from work_pytest.TestDatas import work_datas as wd



@pytest.mark.usefixtures("open_url1")
@pytest.mark.usefixtures("refresh")
class TestLogin:
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", wd.login_data1)
    def test_login(self,open_url1,data):
        lp(open_url1).login(data["phone"],data["pwd"])
