# Copyright 2016 Cloudbase Solutions.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os

if os.name == 'nt':
    from neutron.agent.windows import ip_lib
    from neutron.conf.agent import windows
    OPTS = windows.IP_LIB_OPTS_WINDOWS
else:
    from neutron.agent.linux import ip_lib
    from neutron.conf.agent import linux
    OPTS = linux.IP_LIB_OPTS_LINUX


IPWrapper = ip_lib.IPWrapper
IPDevice = ip_lib.IPDevice
