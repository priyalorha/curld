from mongoengine import *


connect()

class Volume(EmbeddedDocument):

    max = FloatField()
    min = FloatField()
    volume = FloatField()

class TickerInfo(EmbeddedDocument):

    highest_buy_bid = FloatField()
    lowest_sell_bid = FloatField()
    last_traded_price = FloatField()
    yes_price = FloatField()
    volume = EmbeddedDocument(Volume)


class TickerData(Document):

    symbol = StringField()
    info = EmbeddedDocument(TickerInfo)
    timestamp = LongField()
    datetime = LongField()
    high = FloatField()
    low = FloatField(),
    bid = FloatField()
    bidVolume = FloatField()
    ask = FloatField()
    askVolume = FloatField()
    vwap = FloatField()
    open = FloatField()
    close = FloatField()
    last = FloatField()
    baseVolume = FloatField()
    quoteVolume = FloatField()
    previousClose = FloatField()
    change = FloatField()
    percentage = FloatField()
    average = FloatField()

    meta = {
        'strict': False,
        'collection': 'location_data',
        'indexes': 'tickerdata'
    }

    def to_dict(self):
        return {
            'symbol': self.symbol,
            'info': self.info,
            'timestamp': self.timestamp,
            'datetime': self.datetime,
            'high': self.high,
            'low': self.low,
            'bid': self.bid,
            'ask': self.ask,
            'askVolume': self.askVolume,
            'vwap': self.vwap,
            'open': self.open,
            'close': self.close,
            'last': self.last,
            'baseVolume': self.baseVolume,
            'quoteVolume': self.quoteVolume


        }


