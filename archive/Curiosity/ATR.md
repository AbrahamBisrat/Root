# Average True Range (ATR)

## What is ATR?
The Average True Range (ATR) is a technical analysis indicator that measures market **volatility**. It was introduced by J. Welles Wilder Jr. in his book *New Concepts in Technical Trading Systems*. 

Unlike trend indicators (like Moving Averages) or momentum indicators (like RSI), ATR **does not indicate price direction**. It solely answers the question: *"How much is the price typically moving?"*

## Computing the Value
The ATR is calculated based on the "True Range" (TR). The TR is the greatest of the following three values for a given period:
1.  **Current High - Current Low**
2.  **|Current High - Previous Close|**
3.  **|Current Low - Previous Close|**

The **ATR** is essentially a smoothed moving average (typically 14 periods) of these True Range values.

---

## Using ATR for Stop Losses
This is the most practical application of ATR. Using fixed dollar amounts or percentages for stop losses helps, but it often ignores the context of the asset.

*   A $5 drop in a stable utility stock is significant.
*   A $5 drop in a volatile tech stock might be just "noise".

ATR standardizes this by measuring stops in units of volatility rather than currency.

### 1. The "ATR Multiple" Stop
The most common strategy is to place your stop loss at a multiple of the ATR away from your entry price.

**The Formula:**
$$ \text{Stop Price} = \text{Entry Price} \pm (\text{ATR} \times \text{Multiplier}) $$

*   **Long Trade:** Stop = Entry - (ATR * Multiplier)
*   **Short Trade:** Stop = Entry + (ATR * Multiplier)

**Typical Multipliers:**
*   **2 ATR:** Common for trend following.
*   **3 ATR:** Used for longer-term trends to allow for deeper pullbacks.

### 2. The Chandelier Exit (Trailing Stop)
This is a dynamic trailing stop strategy developed by Charles LeBeau. It "hangs" the stop loss from the highest high reached since you entered the trade.

**Formula:**
$$ \text{Stop Price} = \text{Highest High since Entry} - (\text{ATR} \times \text{Multiplier}) $$

As the price makes new highs, the stop moves up. If the price drops, the stop stays flat. This acts as a ratchet, locking in profit while keeping you in the trade as long as the trend is strong.

---

## Example Scenario
Imagine you are trading **Stock XYZ**.

*   **Current Price**: $100
*   **ATR (14-day)**: $2.00 (The stock typically moves $2 a day)
*   **Chosen Multiplier**: 2x

**Setting the Stop:**
You buy at $100.
Stop Loss = $100 - (2.00 * 2) = **$96.00**

**Scenario A: Volatility Increases**
The stock stays at $100, but the market gets nervous. The ATR increases to $3.00.
*   *Note: Standard trailing stops usually stay fixed or move up. If you are calculating dynamic risk before entry, high volatility would tell you to trade SMALLER size because your stop ($6 away) is wider.*

**Scenario B: Price Moves Up**
The stock rallies to $110. The ATR remains $2.00.
New Trailing Stop (Chandelier) = $110 - (2 * 2) = **$106.00**.
You have now locked in $6 of profit per share.

## Summary
*   **High ATR** = High Volatility = Wider Stops needed (Position size should be smaller).
*   **Low ATR** = Low Volatility = Tighter Stops possible (Position size can be larger).

Using ATR allows you to align your risk management with the actual behavior of the market, preventing you from getting "whipsawed" out of trades by normal daily fluctuations.
