from django.db.models.query import QuerySet

from core.schemas.query import PageSchema


class Page:
    def __init__(self, queryset: QuerySet, page: PageSchema) -> None:
        self.queryset = queryset

        self.page_num = page.page_num
        self.page_size = page.page_size

    def total_page(self) -> int:
        return (self.total_count() + self.page_size - 1) // self.page_size

    def total_count(self) -> int:
        return self.queryset.count()

    def get_page_data(self):
        if self.page_num < 1:
            return self.queryset.all()
        return self.queryset.all()[
            (self.page_num - 1) * self.page_size : self.page_num * self.page_size
        ]

    def dict(self):
        return dict(
            data=self.get_page_data(),
            page=dict(
                total_page=self.total_page(),
                total_count=self.total_count(),
                page_num=self.page_num,
                page_size=self.page_size,
            ),
        )
