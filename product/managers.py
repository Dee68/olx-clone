from mptt.managers import TreeManager


class CategoryManager(TreeManager):
    def viewable(self):
        queryset = self.get_queryset().filter(level=0)
        return queryset

    def parentsonly(self):
        queryset = self.get_queryset().filter(level=1)
        return queryset
