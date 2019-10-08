# -*- coding:utf-8 -*-
"""
@author:WangYong
@workNumber:xy04952
@fileName: customPaginator.py
@creatTime: 2019/09/17
"""

from django.core.paginator import Paginator


class KingPaginator(Paginator):
    def __init__(self, object_list, per_page, range_num=2, orphans=0, allow_empty_first_page=True):
        Paginator.__init__(self, object_list, per_page, orphans, allow_empty_first_page)
        self.range_num = range_num

    def page(self, number):
        self.page_num = number
        return super(KingPaginator, self).page(number)

    def _page_range_ext(self):
        num_count = 2 * self.range_num + 1
        if self.num_pages <= num_count:
            return range(1, self.num_pages + 1)
        num_list = []
        num_list.append(self.page_num)
        for i in range(1, self.range_num + 1):
            if self.page_num - i <= 0:
                num_list.append(num_count + self.page_num - i)
            else:
                num_list.append(self.page_num - i)

            if self.page_num + i <= self.num_pages:
                num_list.append(self.page_num + i)
            else:
                num_list.append(self.page_num + i - num_count)
        num_list.sort()
        if self.page_num - 1 > 3:
            num_list.insert(0, '...')
        if self.num_pages - self.page_num > 3:
            num_list.append('...')
        if 1 not in num_list:
            num_list.insert(0, 1)
        if self.num_pages not in num_list:
            num_list.append(self.num_pages)
        return num_list

    page_range_ext = property(_page_range_ext)
