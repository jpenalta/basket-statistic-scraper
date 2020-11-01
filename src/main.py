#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 18:16:11 2020

@author: Juan Penalta Rodríguez y Michaelle Valenzuela Sangoquiza
"""

import os
import csv
import argparse
from LeagueScraperFactory import ScraperFactory
import logging

HEADER_LIST = ['league','game_date','local_team','local_team_points'
               ,'visit_team','visit_team_points'
               ,'player_team','player_name','player_total_points','time'
               ,'one_point_shots_get','one_point_shots_made'
               ,'two_point_shots_get','two_point_shots_made'
               ,'three_point_shots_get','three_point_shots_made'
               ,'rebouts','assists','fouls','received_fouls']
FILE_PATTER = "players_{0}_{1}_{2}.csv"

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

def getfilePaht(league, start_season, end_season):
    current_dir = os.path.dirname(__file__)
    filename = FILE_PATTER.format(league, start_season, end_season)
    return os.path.join(current_dir, filename)
        

def writeToCSV(file_path, player_list):
    with open(file_path, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        for player in player_list:
            writer.writerow(player)

logger = getLogger()
args = getArgs()

logger.info("Get args from command line")
league = args.league
start_season = int(args.startSeason)
end_season = int(args.endSeason)

file_path = getfilePaht(league, start_season, end_season)


logger.info('Create file {0}'.format(file_path))

writeToCSV(file_path, [ HEADER_LIST ])


if( start_season <= end_season):
    logger.info('Get players from {0} between season {1} and season {2}'
                .format(league, start_season, end_season))
    
    logger.info('Get instance for {0} league'. format(league))
    scraperFactory= ScraperFactory(logger)
    league = scraperFactory.getInstance(league)
      
    for season in range(start_season, end_season+1):
        logging.info("Get season {0}".format(season)) 
        player_list = league.getSeasonPlayers(season)
        writeToCSV(file_path, player_list)
              
else:
    print("starSeason must be lower or equal than endSeason")
    



