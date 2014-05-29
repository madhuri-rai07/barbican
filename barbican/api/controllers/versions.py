#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

import pecan

from barbican.api.controllers import handle_exceptions
from barbican.api.controllers import handle_rbac
from barbican.common import utils
from barbican.openstack.common import gettextutils as u
from barbican import version

LOG = utils.getLogger(__name__)


class VersionController(object):

    def __init__(self):
        LOG.debug('=== Creating VersionController ===')

    @pecan.expose('json')
    @handle_exceptions(u._('Version retrieval'))
    @handle_rbac('version:get')
    def index(self):
        return {
            'v1': 'current',
            'build': version.__version__
        }
