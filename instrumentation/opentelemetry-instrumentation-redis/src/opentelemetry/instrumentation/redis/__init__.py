# Copyright The OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Instrument redis to report Redis queries.

opentelemetry-auto-instrumentation will automatically patch your Redis client to make it work.
::

    from opentelemetry.instrumentation.redis.patch import patch
    import redis

    # If not patched yet, you can patch redis specifically
    patch(redis=True)

    # This will report a span with the default settings
    client = redis.StrictRedis(host="localhost", port=6379)
    client.get("my-key")
"""
from opentelemetry.auto_instrumentation.instrumentor import BaseInstrumentor
from opentelemetry.instrumentation.redis.patch import patch, unpatch


class RedisInstrumentor(BaseInstrumentor):
    """An instrumentor for Redis
    See `BaseInstrumentor`
    """

    def _instrument(self):
        patch()

    def _uninstrument(self):
        unpatch()
