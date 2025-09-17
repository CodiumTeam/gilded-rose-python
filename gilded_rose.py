# -*- coding: utf-8 -*-
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE = "Aged Brie"


class GildedRose(object):

    def __init__(self, items):
        self.items = items

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


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

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
