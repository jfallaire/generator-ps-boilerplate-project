#!/bin/sh

sfdx force:auth:jwt:grant \
      -i $SFDX_AUTH_JWT_CONSUMER_KEY \
      -f $SFDX_AUTH_JWT_PRIVATE_KEY_PATH \
      -u $SFDX_AUTH_JWT_USERNAME \
      -r $SFDX_AUTH_JWT_INSTANCE_URL \
      -a $SFDX_AUTH_JWT_ALIAS
      
# will redirect input variables
exec "$@"