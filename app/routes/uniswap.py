from flask import Blueprint, request, jsonify
from services.uniswap_service import get_token_price_usd, get_swap_quote

uniswap_bp = Blueprint("uniswap", __name__)


@uniswap_bp.route("/api/token/price/<symbol>", methods=["GET"])
def token_price(symbol):
    return jsonify(get_token_price_usd(symbol))


@uniswap_bp.route("/api/token/quote", methods=["POST"])
def swap_quote():
    data      = request.json
    token_in  = data.get("tokenIn", "ETH")
    token_out = data.get("tokenOut", "USDC")
    amount    = float(data.get("amountUSD", 0))
    return jsonify(get_swap_quote(token_in, token_out, amount))


@uniswap_bp.route("/api/token/prices", methods=["GET"])
def all_prices():
    symbols = ["ETH", "USDC", "DAI", "USDT", "WBTC"]
    prices  = {s: get_token_price_usd(s) for s in symbols}
    return jsonify(prices)
