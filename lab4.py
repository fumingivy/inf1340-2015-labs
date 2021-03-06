#!/usr/bin/env python3

""" Graded Lab #4 for Inf1340, Fall 2015

    This program computes federal and provincial sales tax.
    Assume that the provincial sales tax is 5 percent and
    the federal sales tax is 2.5 percent. It displays the
    amount of the purchase, the provincial sales tax, the
    federal sales tax, the total tax, and the total of the
    sale.
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Rewrite this code to use global constants, local variables and functions
# Output the text to a file instead of printing it


def bill_of_sale(purchase):

    PROVINCE_SALES_TAX = 0.05
    FEDERAL_SALES_TAX = 0.025
    TOTAL_TAX_RATE = PROVINCE_SALES_TAX + FEDERAL_SALES_TAX
    TOTAL_SALE_MULTIPLIER = 1 + TOTAL_TAX_RATE

    with open("results.txt", "w") as file_results:
        file_results.write("Amount of purchase: {0:.2f}\n".format(purchase))
        file_results.write("Provincial tax: {0:.2f}\n".format(purchase * PROVINCE_SALES_TAX))
        file_results.write("Federal tax: {0:.2f}\n".format(purchase * FEDERAL_SALES_TAX))
        file_results.write("Total tax: {0:.2f}\n".format(purchase * TOTAL_TAX_RATE))
        file_results.write("Total sale: {0:.2f}\n".format(purchase * TOTAL_SALE_MULTIPLIER))

bill_of_sale(100)

