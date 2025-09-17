# -*- coding: utf-8 -*-
from abc import abstractmethod, ABC

SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE = "Aged Brie"


class GildedRose(object):

    def __init__(self, items):
        self.items = []
        for item in items:
            if item.name == AGED_BRIE:
                self.items.append(AgedBrie(item.sell_in, item.quality))
            elif item.name == BACKSTAGE_PASSES:
                self.items.append(BackstagePasses(item.sell_in, item.quality))
            elif item.name == SULFURAS:
                self.items.append(Sulfuras(item.sell_in, item.quality))
            else:
                self.items.append(DefaultItem(item.name, item.sell_in, item.quality))

    def update_quality(self):
        for item in self.items:
            if item.name == AGED_BRIE:
                item.increase_quality()
                item.decrease_sell_in()
                if item.sell_in < 0:
                    item.increase_quality()

            elif item.name == BACKSTAGE_PASSES:
                item.increase_quality()
                if item.sell_in < 11:
                    item.increase_quality()
                if item.sell_in < 6:
                    item.increase_quality()
                item.decrease_sell_in()
                if item.sell_in < 0:
                    item.quality = 0

            elif item.name == SULFURAS:
                pass

            # the rest of the products
            else:
                item.decrease_quality()
                item.decrease_sell_in()
                if item.sell_in < 0:
                    item.decrease_quality()


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
        pass


class BackstagePasses(Item):
    def __init__(self, sell_in, quality):
        super().__init__(BACKSTAGE_PASSES, sell_in, quality)

    def update_state(self):
        pass


class Sulfuras(Item):
    def __init__(self, sell_in, quality):
        super().__init__(SULFURAS, sell_in, quality)

    def update_state(self):
        pass


class DefaultItem(Item):
    def update_state(self):
        pass