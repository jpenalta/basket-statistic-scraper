#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 08:03:57 2020

@author: juanpr
"""
from  ACBStatisticsScraper import ACBScraper

ACB = "acb"

class ScraperFactory:
    
    def __init__(self, logger):
        self.logger = logger
        
    def getInstance(self, league):
        
        factory = None
        
        if(league == ACB): 
            factory = ACBScraper(self.logger)
        else: 
            self.logger.error("The factory not exists, valid factorys are: acb,...")
               
        return factory