from TensorPage import Stage_1, Stage_2
import logging
logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode='w')
logger = logging.getLogger(__name__)


def test_stage_1(browser):
    tensor_page = Stage_1(browser)
    tensor_page.go_to_site()
    tensor_page.click_Contacts()
    tensor_page.click_banner_tensor()
    powerInHuman = tensor_page.check_power_in_human()
    aboutPowerInHuman = tensor_page.open_power_in_human_about()
    checkBlockWorkHW = tensor_page.check_block_work_h_w()
    assert powerInHuman and aboutPowerInHuman == "https://tensor.ru/about" and checkBlockWorkHW


def test_stage_2(browser):
    tensor_page = Stage_2(browser)
    tensor_page.go_to_site()
    tensor_page.click_Contacts()
    region_1 = tensor_page.check_region("Владимирская обл.")
    newListPartner = tensor_page.check_list_partner()
    tensor_page.edit_region()
    oldListPartner = tensor_page.check_list_partner()
    region_2 = tensor_page.check_region("Камчатский край")
    urlTitle = tensor_page.check_url_title_41()
    assert region_1 \
           and len(newListPartner) > 0 \
           and len(oldListPartner) > 0 \
           and newListPartner != oldListPartner \
           and region_2 and urlTitle
