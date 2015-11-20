import mediacloud, json, datetime, ConfigParser, logging

config = ConfigParser.ConfigParser()
config.read('template_config.cfg')

logging.basicConfig(filename='hw2logfile.log' , level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Start Logging')

def APIcall():
	my_api_key = 'my_api_key'
	mc = mediacloud.api.MediaCloud(my_api_key)
	bees_2013 = mc.sentenceCount('( bee OR bees)', solr_filter=[mc.publish_date_query( datetime.date( 2013, 1, 1), datetime.date( 2014, 1, 1) ), 'media_sets_id:1' ])
	bees_2014 = mc.sentenceCount('( bee OR bees)', solr_filter=[mc.publish_date_query( datetime.date( 2014, 1, 1), datetime.date( 2015, 1, 1) ), 'media_sets_id:1' ])
	return (bees_2013, bees_2014)

bees_2013, bees_2014 = APIcall()
year_with_more_mentions = '2014' if bees_2014['count'] > bees_2013['count'] else '2013'
print "Bees were mentioned more times in %s" % year_with_more_mentions
print "%d mentions in 2014, %d mentions in 2013"% (bees_2014['count'],bees_2013['count'])