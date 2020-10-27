#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 18:16:11 2020

@author: Juan Penalta Rodríguez y Michaelle Valenzuela Sangoquiza
"""

import os
import csv
import argparse
from  ACBStatisticsScraper import ACBScraper
import logging

HEADER_LIST = ['league','game_date','local_team','local_team_points'
               ,'visit_team','visit_team_points'
               ,'player_team','player_name','player_total_points','time'
               ,'one_point_shots_get','one_point_shots_made'
               ,'two_point_shots_get','two_point_shots_made'
               ,'three_point_shots_get','three_point_shots_made'
               ,'rebouts','assists','fouls','received_fouls']

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--startSeason", help="Enter start season of interval")
    parser.add_argument("--endSeason", help="Enter end season of interval")
    parser.add_argument("--league", help="Enter league: acb")
    args = parser.parse_args()
    return args

def getLogger():
    # create logger
    logger = logging.getLogger('basketScraper')
    logger.setLevel(logging.DEBUG)
    
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # add formatter to ch
    ch.setFormatter(formatter)
    
    # add ch to logger
    logger.addHandler(ch)
    
    return logger


logger = getLogger()
args = getArgs()

league = args.league
start_season = int(args.startSeason)
end_season = int(args.endSeason)

currentDir = os.path.dirname(__file__)
filename = "players_{0}_{1}_{2}.csv".format(league, start_season, end_season)
filePath = os.path.join(currentDir, filename)

player_list = []
player_list.append(HEADER_LIST)

logger.info('Create file {0}'.format(filename))
    
logger.info('Get players from {0} between season {1} and season {2}'.format(league, start_season, end_season))

if( start_season <= end_season):
    acb = ACBScraper(logger)
    for season in range(start_season,end_season+1):
        logging.info("Get season {0}".format(season)) 
        player_list = player_list + acb.getSeasonPlayers(season)
else:
    print("StarSeason must be lower or equal than endSeason")
    
with open(filePath, 'w', newline='') as csvFile:
  writer = csv.writer(csvFile)
  for player in player_list:
    writer.writerow(player)


