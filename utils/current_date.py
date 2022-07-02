# -*- coding: utf-8 -*-
import datetime
import calendar


class MyDate:

    def __init__(self):
        self.now = datetime.datetime.today()

    def current_day(self):
        """
        return today date
        """
        today_str = self.now.strftime('%Y%m%d')
        today_date = self.now.strftime('%Y-%m-%d')
        return today_str,today_date

    def tomorrow(self):
        """
        return tomorrow date
        """
        tomorrow = self.now + datetime.timedelta(days=1)
        tmr_str = tomorrow.strftime('%Y%m%d')
        tmr_date = tomorrow.strftime('%Y-%m-%d')
        return tmr_str,tmr_date

    def yesterday(self):
        """
        return yesterday date
        """
        yesterday = self.now - datetime.timedelta(days=1)
        yst_str = yesterday.strftime('%Y%m%d')
        yst_date = yesterday.strftime('%Y-%m-%d')
        return yst_str,yst_date


    def lastweek(self):
        """
        return last weeek
        """
        last_week_s = self.now - datetime.timedelta(days=self.now.weekday() + 7)
        last_week_e = self.now - datetime.timedelta(days=self.now.weekday() + 1)
        last_week_s_str = last_week_s.strftime('%Y%m%d')
        last_week_e_str = last_week_e.strftime('%Y%m%d')
        last_week_s_date = last_week_s.strftime('%Y-%m-%d')
        last_week_e_date = last_week_e.strftime('%Y-%m-%d')
        return last_week_s_str,last_week_s_date,last_week_e_str,last_week_e_date

    def currentweek(self):
        """
        return current week
        """
        current_w_s = self.now - datetime.timedelta(days=self.now.weekday())
        current_w_e = self.now + datetime.timedelta(days = 6-
                self.now.weekday())
        current_w_e_str = current_w_e.strftime('%Y%m%d')
        current_w_e_date = current_w_e.strftime('%Y-%m-%d')
        current_w_s_str = current_w_s.strftime('%Y%m%d')
        current_w_s_date = current_w_s.strftime('%Y-%m-%d')
        return current_w_s_str,current_w_s_date,current_w_e_str,current_w_e_date

    def nextweek(self):
        """
        return next week
        """
        next_w_s = self.now + datetime.timedelta(days = 7 - self.now.weekday())
        next_w_e = self.now + datetime.timedelta(days = 13 - self.now.weekday())
        next_w_s_str = next_w_s.strftime('%Y%m%d')
        next_w_s_date = next_w_s.strftime('%Y-%m-%d')
        next_w_e_str = next_w_e.strftime('%Y%m%d')
        next_w_e_date = next_w_e.strftime('%Y-%m-%d')
        return next_w_s_str,next_w_s_date,next_w_e_str,next_w_e_date

    def lastmonth(self):
        """
        return next month
        """
        pass

    def currentmonth(self):
        """
        return current month
        """
        current_m_s = datetime.datetime.today().replace(day=1)
        current_m_e = self.now.replace(day=calendar.monthrange(self.now.year,self.now.month)[1])
        current_m_s_str = current_m_s.strftime('%Y%m%d')
        current_m_s_date = current_m_s.strftime('%Y-%m-%d')
        current_m_e_str = current_m_e.strftime('%Y%m%d')
        current_m_e_date = current_m_e.strftime('%Y-%m-%d')
        return current_m_s_str,current_m_s_date,current_m_e_str,current_m_e_date

    def nextmonth(self):
        """
        return next month
        """
        pass

