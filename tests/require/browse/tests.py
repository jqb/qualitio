# -*- coding: utf-8 -*-
from selenium import selenium
from config import settings
import unittest, time, base64

class BaseSeleniumTestCase(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 
                                 4444, 
                                 "*%s" % settings['browser'], 
                                 settings['hostname'])
        
        if settings['username']:
            self.selenium.addCustomRequestHeader("Authorization", "Basic %s" % 
                                                 base64.b64encode("%s:%s" % (settings['username'], settings['password'])).strip())
        self.selenium.start()

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)


class HeaderpageVerifytext(BaseSeleniumTestCase):
    
    def test_headerpage_verifytext(self):
        sel = self.selenium
        sel.open("/require/#requirement/1/details/")
        sel.click("link=MeeGo")
        try: self.assertEqual("qualitio: requirements", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        self.failUnless(sel.is_element_present("css=#logo"))
        try: self.assertEqual("qualitiorequirements", sel.get_text("css=#logo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        self.failUnless(sel.is_element_present("css=#notification.notify-wrapper-oneattime"))
        try: self.assertEqual("requirments", sel.get_text("link=requirments"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("store", sel.get_text("link=store"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("execute", sel.get_text("link=execute"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("report", sel.get_text("link=report"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("settings", sel.get_text("link=settings"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("admin", sel.get_text("link=admin"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        self.failUnless(sel.is_element_present("css=#application-menu"))
        try: self.assertEqual("browse", sel.get_text("css=#application-menu ul li"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("filter", sel.get_text("css=#application-menu ul li a"))
        except AssertionError, e: self.verificationErrors.append(str(e))


class TreeVerifyelements(BaseSeleniumTestCase):
    
    def test_tree_verifyelements(self):
        sel = self.selenium
        sel.open("/require/#requirement/1/details/")
        for i in range(60):
            try:
                if sel.is_text_present("MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=MeeGo")
        try: self.assertEqual("qualitio: requirements", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "Notebook" == sel.get_text("link=Notebook"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=Notebook"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=li#2 a ins"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=li#1 ins"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("css=li#1 ins")
        sel.click("css=li#1 ins")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=li#2 ins"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=li#4 a ins"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=li#4 ins"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("css=li#4 ins")
        sel.click("css=li#4 ins")
        for i in range(60):
            try:
                if sel.is_element_present("link=Bootscreen"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("css=li#8 ins"))
        except AssertionError, e: self.verificationErrors.append(str(e))


class Newreq(BaseSeleniumTestCase):
    
    def test_newreq(self):
        sel = self.selenium
        sel.open("/require/#requirement/1/details/")
        try: self.assertEqual("qualitio: requirements", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
	time.sleep(2)
        for i in range(60):
            try:
                if sel.is_text_present("exact:requirement: TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("css=div#application-view-footer div a span")
        for i in range(60):
            try:
                if "new requirement" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(2)
        else: self.fail("time out")
        sel.type("id_name", "new requirement 1")
        sel.click("id_release_target")
        for i in range(60):
            try:
                if sel.is_element_present("css=div#ui-datepicker-div div div"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=1")
        sel.click("release_target_wrapper")
        for i in range(60):
            try:
                if sel.is_text_present("new requirement"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("Executed")
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=MeeGo")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_text_present("TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=TV")
        for i in range(60):
            try:
                if sel.is_element_present("link=new requirement 1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=new requirement 1"))
        except AssertionError, e: self.verificationErrors.append(str(e))


class Modreq(BaseSeleniumTestCase):
    
    def test_modreq(self):
        sel = self.selenium
        sel.open("/require/#requirement/1/details/")
        try: self.assertEqual("qualitio: requirements", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
	time.sleep(2)
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
	time.sleep(3)
        for i in range(60):
            try:
                if sel.is_text_present("exact:requirement: TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("css=div#application-view-footer div a span")
        for i in range(60):
            try:
                if "new requirement" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(2)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("id_name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.type("id_name", "new requirement 2")
        sel.click("id_release_target")
        for i in range(60):
            try:
                if sel.is_element_present("css=div#ui-datepicker-div div div"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=1")
        sel.click("release_target_wrapper")
        for i in range(60):
            try:
                if sel.is_text_present("new requirement"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("Executed")
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        time.sleep(2)
	sel.click("link=MeeGo")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        time.sleep(2)
	sel.click("link=TV")
        for i in range(60):
            try:
                if sel.is_element_present("link=new requirement 2"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=new requirement 2"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=new requirement 2")
        sel.click("link=new requirement 2")
        for i in range(60):
            try:
                if "requirement: new requirement 2" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.failUnless(sel.is_element_present("css=div#application-view-header h1"))
        sel.click("link=edit")
        for i in range(60):
            try:
                if sel.is_element_present("id_name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.type("id_name", "mod requirement 3")
        sel.click("css=input.ui-button")
        for i in range(60):
            try:
                if sel.is_element_present("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=MeeGo")
	time.sleep(2)
        for i in range(60):
            try:
                if sel.is_text_present("exact:requirement: MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "Notebook" == sel.get_text("link=Notebook"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
        for i in range(60):
            try:
                if sel.is_element_present("link=mod requirement 3"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("link=mod requirement 3")
        for i in range(60):
            try:
                if "requirement: mod requirement 3" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("exact:requirement: mod requirement 3"))
        except AssertionError, e: self.verificationErrors.append(str(e))


class Test5TestcasesDel(BaseSeleniumTestCase):
    
    def test_5_testcases_del(self):
        sel = self.selenium
        sel.set_timeout("10000")
        sel.open("/require/#requirement/13/details/")
        for i in range(60):
            try:
                if sel.is_text_present("qualitiorequirements"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
        for i in range(60):
            try:
                if "requirement: MeeGo" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
        for i in range(60):
            try:
                if "requirement: TV" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("requirement: TV", sel.get_text("css=div#application-view-header h1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("link=MeeGo Handset test"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "MeeGo Handset test" == sel.get_text("link=MeeGo Handset test"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo Handset test"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo Handset test")
        for i in range(60):
            try:
                if "requirement: MeeGo Handset test" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("requirement: MeeGo Handset test", sel.get_text("css=div#application-view-header h1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "test cases" == sel.get_text("link=test cases"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=test cases"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=test cases")
        for i in range(60):
            try:
                if sel.is_text_present("del"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("del"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("disconnect"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("disconnect")
        for i in range(60):
            try:
                if sel.is_element_present("save"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("save"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("save")
        for i in range(60):
            try:
                if sel.is_element_present("id_search"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_search"))
        except AssertionError, e: self.verificationErrors.append(str(e))


class Test6TestcasesAdd(BaseSeleniumTestCase):
    
    def test_6_testcases_add(self):
        sel = self.selenium
        sel.set_timeout("10000")
        sel.open("/require/#requirement/13/details/")
        for i in range(60):
            try:
                if sel.is_text_present("qualitiorequirements"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "MeeGo" == sel.get_text("link=MeeGo"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo")
        for i in range(60):
            try:
                if "requirement: MeeGo" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "TV" == sel.get_text("link=TV"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=TV"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=TV")
        for i in range(60):
            try:
                if "requirement: TV" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("requirement: TV", sel.get_text("css=div#application-view-header h1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("link=MeeGo Handset test"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "MeeGo Handset test" == sel.get_text("link=MeeGo Handset test"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=MeeGo Handset test"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=MeeGo Handset test")
        for i in range(60):
            try:
                if "requirement: MeeGo Handset test" == sel.get_text("css=div#application-view-header h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("requirement: MeeGo Handset test", sel.get_text("css=div#application-view-header h1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "test cases" == sel.get_text("link=test cases"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=test cases"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=test cases")
        for i in range(60):
            try:
                if sel.is_element_present("id_search"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_search"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("id_search", "Mee")
        try: self.failUnless(sel.is_element_present("id_search_submit"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("id_search_submit")
        for i in range(60):
            try:
                if sel.is_element_present("connect"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("connect"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("connect")
        try: self.failUnless(sel.is_element_present("save"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("save")
        for i in range(60):
            try:
                if sel.is_text_present("#1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("#1"))
        except AssertionError, e: self.verificationErrors.append(str(e))


if __name__ == "__main__":
    unittest.main()