from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.sites.shortcuts import get_current_site

# First we create a little helper function, becase we will potentially have many PaginatedTypes 
# and we will potentially want to turn many querysets into paginated results:

def get_paginator(qs, page_size, page, base_url, paginated_type, **kwargs):
    p = Paginator(qs, page_size)
    try:
        page_obj = p.page(page)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        return paginated_type(
            count=p.count,
            currentPage=page,
            totalPages=p.num_pages,
            next=None,
            prev=None,
            results=None,
            **kwargs
        )

    query_next = "{exchanges(page:" + str(page + 1) + "){count currentPage totalPages next prev results{id toyToChange desiredToy active owner{id name contact} pictures{id imageUrl}}}}"
    query_prev = "{exchanges(page:" + str(page - 1) + "){count currentPage totalPages next prev results{id toyToChange desiredToy active owner{id name contact} pictures{id imageUrl}}}}"

    return paginated_type(
        count=p.count,
        currentPage=page_obj.number,
        totalPages=p.num_pages,
        next=base_url+"#query="+query_next if page_obj.has_next() else None,
        prev=base_url+"#query="+query_prev if page_obj.has_previous() else None,
        results=page_obj.object_list,
        **kwargs
    )