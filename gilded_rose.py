# -*- coding: utf-8 -*-
from abc import abstractmethod, ABC

SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE = "Aged Brie"


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_state()


class Item(ABC):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    @abstractmethod
    def update_state(self):
        pass

    def increase_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1

    def decrease_quality(self):
        if self.quality > 0:
            self.quality = self.quality - 1

    def decrease_sell_in(self):
        self.sell_in = self.sell_in - 1

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class AgedBrie(Item):
    def __init__(self, sell_in, quality):
        super().__init__(AGED_BRIE, sell_in, quality)

    def update_state(self):
        self.increase_quality()
        self.decrease_sell_in()
        if self.sell_in < 0:
            self.increase_quality()


class BackstagePasses(Item):
    def __init__(self, sell_in, quality):
        super().__init__(BACKSTAGE_PASSES, sell_in, quality)

    def update_state(self):
        self.increase_quality()
        if self.sell_in < 11:
            self.increase_quality()
        if self.sell_in < 6:
            self.increase_quality()
        self.decrease_sell_in()
        if self.sell_in < 0:
            self.quality = 0


class Sulfuras(Item):
    def __init__(self, sell_in, quality):
        super().__init__(SULFURAS, sell_in, quality)

    def update_state(self):
        pass


class DefaultItem(Item):
    def update_state(self):
        self.decrease_quality()
        self.decrease_sell_in()
        if self.sell_in < 0:
            self.decrease_quality()