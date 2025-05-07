from typing import Literal

class Currency:
    """
    Base Class for Currency.
    """
    def __init__(
            self,
            name: str,
            irt: str,
            usdt: str,
            symbol: str,
        ) -> None:
        """
        Initiation.
        
        Args:
            name (str): Name of the currency.
            upper (str): Upper case name of the currency.
            lower (str): Lower case name of the currency.
            symbol (str): Symbol of the currency.
        """
        self.name = name
        self.irt = irt
        self.usdt = usdt
        self.symbol = symbol

        self._dict = {
            "name": name,
            "irt": irt,
            "usdt": usdt,
            "symbol": symbol,
        }

    def get(self, currency: Literal['irt', 'usdt', 'symbol']) -> str:
        result = self._dict[currency]
        if result: return result
        else: raise ValueError(f"Invalid currency: {currency}")

    def __str__(self) -> str:
        return self.name

class CurrencyManager:
    """
    Class to manage currencies.
    """

    all = Currency('all', 'all', 'all', 'all')
    rial = Currency('rial', 'RLS', 'RLS', 'rls')

    inch = Currency('1inch', '1INCHIRT', '1INCHUSDT', '1inch')
    aave = Currency('aave', 'AAVEIRT', 'AAVEUSDT', 'aave')
    ada = Currency('ada', 'ADAIRT', 'ADAUSDT', 'ada')
    agld = Currency('agld', 'AGLDIRT', 'AGLDUSDT', 'agld')
    algo = Currency('algo', 'ALGOIRT', 'ALGOUSDT', 'algo')
    ant = Currency('ant', 'ANTIRT', 'ANTUSDT', 'ant')
    api3 = Currency('api3', 'API3IRT', 'API3USDT', 'api3')
    apt = Currency('apt', 'APTIRT', 'APTUSDT', 'apt')
    avax = Currency('avax', 'AVAXIRT', 'AVAXUSDT', 'avax')
    axs = Currency('axs', 'AXSIRT', 'AXSUSDT', 'axs')
    band = Currency('band', 'BANDIRT', 'BANDUSDT', 'band')
    bat = Currency('bat', 'BATIRT', 'BATUSDT', 'bat')
    bch = Currency('bch', 'BCHIRT', 'BCHUSDT', 'bch')
    blur = Currency('blur', 'BLURIRT', 'BLURUSDT', 'blur')
    bnb = Currency('bnb', 'BNBIRT', 'BNBUSDT', 'bnb')
    btc = Currency('btc', 'BTCIRT', 'BTCUSDT', 'btc')
    celr = Currency('celr', 'CELRIRT', 'CELRUSDT', 'celr')
    comp = Currency('comp', 'COMPIRT', 'COMPUSDT', 'comp')
    crv = Currency('crv', 'CRVIRT', 'CRVUSDT', 'crv')
    cvx = Currency('cvx', 'CVXIRT', 'CVXUSDT', 'cvx')
    dai = Currency('dai', 'DAIIRT', 'DAIUSDT', 'dai')
    dao = Currency('dao', 'DAOIRT', 'DAOUSDT', 'dao')
    doge = Currency('doge', 'DOGEIRT', 'DOGEUSDT', 'doge')
    dot = Currency('dot', 'DOTIRT', 'DOTUSDT', 'dot')
    dydx = Currency('dydx', 'DYDXIRT', 'DYDXUSDT', 'dydx')
    egala = Currency('egala', 'EGALAIRT', 'EGALAUSDT', 'egala')
    enj = Currency('enj', 'ENJIRT', 'ENJUSDT', 'enj')
    ens = Currency('ens', 'ENSIRT', 'ENSUSDT', 'ens')
    eos = Currency('eos', 'EOSIRT', 'EOSUSDT', 'eos')
    etc = Currency('etc', 'ETCIRT', 'ETCUSDT', 'etc')
    eth = Currency('eth', 'ETHIRT', 'ETHUSDT', 'eth')
    ethfi = Currency('ethfi', 'ETHFIIRT', 'ETHFIUSDT', 'ethfi')
    fet = Currency('fet', 'FETIRT', 'FETUSDT', 'fet')
    fil = Currency('fil', 'FILIRT', 'FILUSDT', 'fil')
    flow = Currency('flow', 'FLOWIRT', 'FLOWUSDT', 'flow')
    ftm = Currency('ftm', 'FTMIRT', 'FTMUSDT', 'ftm')
    gal = Currency('gal', 'GALIRT', 'GALUSDT', 'gal')
    glm = Currency('glm', 'GLMIRT', 'GLMUSDT', 'glm')
    gmx = Currency('gmx', 'GMXIRT', 'GMXUSDT', 'gmx')
    grt = Currency('grt', 'GRTIRT', 'GRTUSDT', 'grt')
    gmt = Currency('gmt', 'GMTIRT', 'GMTUSDT', 'gmt')
    hbar = Currency('hbar', 'HBARIRT', 'HBARUSDT', 'hbar')
    imx = Currency('imx', 'IMXIRT', 'IMXUSDT', 'imx')
    jst = Currency('jst', 'JSTIRT', 'JSTUSDT', 'jst')
    link = Currency('link', 'LINKIRT', 'LINKUSDT', 'link')
    ldo = Currency('ldo', 'LDOIRT', 'LDOUSDT', 'ldo')
    lpt = Currency('lpt', 'LPTIRT', 'LPTUSDT', 'lpt')
    lrc = Currency('lrc', 'LRCIRT', 'LRCUSDT', 'lrc')
    ltc = Currency('ltc', 'LTCIRT', 'LTCUSDT', 'ltc')
    magic = Currency('magic', 'MAGICIRT', 'MAGICUSDT', 'magic')
    mana = Currency('mana', 'MANAIRT', 'MANAUSDT', 'mana')
    matic = Currency('matic', 'MATICIRT', 'MATICUSDT', 'matic')
    mdt = Currency('mdt', 'MDTIRT', 'MDTUSDT', 'mdt')
    meme = Currency('meme', 'MEMEIRT', 'MEMEUSDT', 'meme')
    mkr = Currency('mkr', 'MKRIRT', 'MKRUSDT', 'mkr')
    near = Currency('near', 'NEARIRT', 'NEARUSDT', 'near')
    not_ = Currency('not', 'NOTIRT', 'NOTUSDT', 'not')
    nmr = Currency('nmr', 'NMRIRT', 'NMRUSDT', 'nmr')
    omg = Currency('omg', 'OMGIRT', 'OMGUSDT', 'omg')
    om = Currency('om', 'OMIRT', 'OMUSDT', 'om')
    one = Currency('one', 'ONEIRT', 'ONEUSDT', 'one')
    qnt = Currency('qnt', 'QNTIRT', 'QNTUSDT', 'qnt')
    rdnt = Currency('rdnt', 'RDNTIRT', 'RDNTUSDT', 'rdnt')
    rndr = Currency('rndr', 'RNDRIRT', 'RNDRUSDT', 'rndr')
    rsr = Currency('rsr', 'RSRIRT', 'RSRUSDT', 'rsr')
    sand = Currency('sand', 'SANDIRT', 'SANDUSDT', 'sand')
    shib = Currency('shib', 'SHIBIRT', 'SHIBUSDT', 'shib')
    skl = Currency('skl', 'SKLIRT', 'SKLUSDT', 'skl')
    slp = Currency('slp', 'SLPIRT', 'SLPUSDT', 'slp')
    snx = Currency('snx', 'SNXIRT', 'SNXUSDT', 'snx')
    sol = Currency('sol', 'SOLIRT', 'SOLUSDT', 'sol')
    storj = Currency('storj', 'STORJIRT', 'STORJUSDT', 'storj')
    ssv = Currency('ssv', 'SSVIRT', 'SSVUSDT', 'ssv')
    sushi = Currency('sushi', 'SUSHIIRT', 'SUSHIUSDT', 'sushi')
    ton = Currency('ton', 'TONIRT', 'TONUSDT', 'ton')
    trx = Currency('trx', 'TRXIRT', 'TRXUSDT', 'trx')
    trb = Currency('trb', 'TRBIRT', 'TRBUSDT', 'trb')
    uni = Currency('uni', 'UNIIRT', 'UNIUSDT', 'uni')
    uma = Currency('uma', 'UMAIRT', 'UMAUSDT', 'uma')
    usdc = Currency('usdc', 'USDCIRT', 'USDCUSDT', 'usdc')
    usdt = Currency('usdt', 'USDTIRT', 'USDTUSDT', 'usdt')
    w = Currency('w', 'WIRT', 'WUSDT', 'w')
    wbtc = Currency('wbtc', 'WBTCIRT', 'WBTCUSDT', 'wbtc')
    woo = Currency('woo', 'WOOIRT', 'WOOUSDT', 'woo')
    wld = Currency('wld', 'WLDIRT', 'WLDUSDT', 'wld')
    xlm = Currency('xlm', 'XLMIRT', 'XLMUSDT', 'xlm')
    xmr = Currency('xmr', 'XMRIRT', 'XMRUSDT', 'xmr')
    xrp = Currency('xrp', 'XRPIRT', 'XRPUSDT', 'xrp')
    xtz = Currency('xtz', 'XTZIRT', 'XTZUSDT', 'xtz')
    yfi = Currency('yfi', 'YFIIRT', 'YFIUSDT', 'yfi')
    zro = Currency('zro', 'ZROIRT', 'ZROUSDT', 'zro')
    zrx = Currency('zrx', 'ZRXIRT', 'ZRXUSDT', 'zrx')
