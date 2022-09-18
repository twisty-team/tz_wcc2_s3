from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.sites.shortcuts import get_current_site


def get_paginator(qs, page_size, page, paginated_type, **kwargs):
    p = Paginator(qs, page_size)
    try:
        page_obj = p.page(page)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        return paginated_type(
            count=p.count,
            page_size=page_size,
            current_page=page,
            total_pages=p.num_pages,
            has_next=False,
            has_prev=False,
            excahnges=None,
            **kwargs
        )

    return paginated_type(
        count=p.count,
        page_size=page_size,
        current_page=page_obj.number,
        total_pages=p.num_pages,
        has_next=page_obj.has_next(),
        has_prev=page_obj.has_previous(),
        exchanges=page_obj.object_list,
        **kwargs
    )