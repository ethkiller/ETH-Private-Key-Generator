import base64, codecs
magic = 'ZnJvbSBjb2xvcmFtYSBpbXBvcnQgaW5pdA0KaW5pdCgpDQpmcm9tIGNvbG9yYW1hIGltcG9ydCBGb3JlDQppbXBvcnQgcmFuZG9tDQppbXBvcnQgc3RyaW5nDQppbXBvcnQgdGltZQ0KaW1wb3J0IHJhbmRvbQ0KaW1wb3J0IG9zDQppbXBvcnQgZWNkc2ENCg0KDQoNCg0KcHJpbnQoRm9yZS5HUkVFTiArICIiIg0K4pWU4pWQ4pWQ4pWQ4pWm4pWQ4pWQ4pWQ4pWQ4pWm4pWX4pSA4pWU4pWXICDilZTilZfilZTilZDilabilZDilZDilabilZfilIDilIDilZTilZfilIDilIDilZTilZDilZDilZDilabilZDilZDilZDilZcNCuKVkeKVlOKVkOKVkOKVo+KVlOKVl+KVlOKVl+KVkeKVkeKUgOKVkeKVkSAg4pWR4pWR4pWR4pWU4pWp4pWj4pWg4pWj4pWR4pSA4pSA4pWR4pWR4pSA4pSA4pWR4pWU4pWQ4pWQ4pWj4pWU4pWQ4pWX4pWRDQrilZHilZrilZDilZDilazilZ3ilZHilZHilZrilaPilZrilZDilZ3ilZEgIOKVkeKVmuKVneKVneKUgOKVkeKVkeKVkeKVkeKUgOKUgOKVkeKVkeKUgOKUgOKVkeKVmuKVkOKVkOKVo+KVmuKVkOKVneKVkQ0K4pWR4pWU4pWQ4pWQ4pWd4pSA4pWR4pWR4pSA4pWR4pWU4pWQ4pWX4pWRICDilZHilZTilZfilZHilIDilZHilZHilZHilZHilIDilZTilaPilZHilIDilZTilaPilZTilZDilZDilaPilZTilZfilZTilZ0NCuKVkeKVmuKVkOKVkOKVl+KUgOKVkeKVkeKUgOKVkeKVkeKUgOKVkeKVkSAg4pWR4pWR4pWR4pWa4pWm4pWj4pWg4pWj4pWa4pWQ4pWd4pWR4pWa4pWQ4pWd4pWR4pWa4pWQ4pWQ4pWj4pWR4pWR4pWa4pWXDQrilZrilZDilZDilZDilZ3ilIDilZrilZ3ilIDilZr'
love = 'vyM3vyVQvyMevyM0tVBXIzhXIarXIzhXIxBXIdrXIxBXIxBXIdrXIxBXIxBXIxBXIdrXIxBXIxBXIxBXIdrXIxBXIxBXIxBXIdrXIarXIzhXIxBXIaD0XVvVvXD0XQDcjpzyhqPuTo3WyYxqFEHIBVPftVxIHFPOYFHkZEIVtHUWcqzS0MFOYMKxtD2uyL2gypv4tKT4vXD0XQDcuoaA3MKVtCFOcoaO1qPtvFJLtrJ91VUquoaDtqT8tL29hqTyhqJHfVUOlMKAmVQSpoxyzVUyiqFO3LJ50VUEiVUO1pzAbLKAyVUEbMFOzqJkfVUMypaAco24fVUOlMKAmVQVtKT4vXD0XnJLtLJ5mq2IlVPR9VPVkVvOuozDtLJ5mq2IlVPR9VPVlVwbAPvNtVPOjpzyhqPtvEKucqTyhMl4hYvVcQDbtVPNtMKucqPtcQDcyoTyzVTShp3qypvN9CFNvZvV6QDbtVPNtpUWcoaDbEz9lMF5MEHkZG1ptXlNvD29hqTSwqPONpzIuoTI0nTgcoTkypvOiovOHMJkyM3WuoFOzo3VtoJ9lMFOcozMiYvVcQDbtVPNtnJ5jqKDbEz9lMF5MEHkZG1ptXlNvVvxAPvNtVPOkqJy0XPxAPvNtVPNAPt0XMaWioFOwo2kipzSgLFOcoKOipaDtnJ5cqN0XnJ5cqPtcQDczpz9gVTAioT9lLJ1uVTygpT9lqPOTo3WyQDccoKOipaDtpzShMT9gQDccoKOipaDtp3ElnJ5aQDccoKOipaDtqTygMD0XnJ1jo3W0VT9mQDbAPzEyMvOaMJ5ypzS0MI9lLJ5xo21sLJExpzImpltcBt0XVPNtVTSxMUWyp3ZtCFNaZUtaVPftWlphnz9covulLJ5xo20hL2uinJAyXUA0pzyhMl5bMKuxnJqcqUZcVTMipvOsVTyhVUWuozqyXQDjXFxAPvNtVPOlMKE1pz4tLJExpzImpj0XQDcxMJLtM2IhMKWuqTIsMzyhLJksLJExpzImpltcBt0XVPNtVTSxMUWyp3ZtCFNaZUtaVPftWlphnz9cov'
god = 'hyYW5kb20uY2hvaWNlKHN0cmluZy5oZXhkaWdpdHMpIGZvciBfIGluIHJhbmdlKDEwKSkNCiAgICByZXR1cm4gYWRkcmVzcyAgICANCg0KZGVmIGdlbmVyYXRlX3ByaXZhdGVfa2V5KCk6DQogICAgcHJpdmF0ZV9rZXkgPSAnJy5qb2luKHJhbmRvbS5jaG9pY2UocGFwZXJzKSBmb3IgXyBpbiByYW5nZSg2NCkpDQogICAgcmV0dXJuIHByaXZhdGVfa2V5ICAgIA0KDQpkZWYgZ2VuZXJhdGVfYmFsYW5jZSgpOg0KICAgIGJhbGFuY2UgPSAnJy5qb2luKHJhbmRvbS5jaG9pY2UobnVtYmVycykgZm9yIF8gaW4gcmFuZ2UoMikpDQogICAgcmV0dXJuIGJhbGFuY2UgICAgDQoNCmRlZiBnZW5lcmF0ZV9iYWxhbmNlX2xvdygpOg0KICAgIGJhbGFuY2UgPSAnJy5qb2luKHJhbmRvbS5jaG9pY2UobnVtYmVyc19sb3cpIGZvciBfIGluIHJhbmdlKDEpKQ0KICAgIHJldHVybiBiYWxhbmNlICAgICANCg0KcGFwZXJzID0gWydhJywnYicsJ2MnLCdkJywnZScsJ2YnLCcwJywnMScsJzInLCczJywnNCcsJzUnLCc2JywnNycsJzgnLCc5J10gDQoNCm51bWJlcnMgPSBbJzEnLCcyJywnMycsJzQnLCc1JywnNicsJzcnLCc4JywnOScsJzAnXSANCg0KbnVtYmVyc19sb3cgPSBbJzEnLCcyJywnMycsJzQnLCc1JywnMCddIA0KDQoNCm51bWJlcl9vZl9hZGRyZXNzZXMgPSByYW5kb20ucmFuZGludCgxMDAwLCAxNTAwKQ0KZm9yIGkgaW4gcmFuZ2UobnVtYmVyX29mX2FkZHJlc3Nlcyk6DQogICAgcHJpbnQoRm9yZS5SRUQgKyAiR2VuZXJhdGluZyBhZGRyZXNzOiAiK2dlbmVyYXRlX3JhbmRvbV9hZGRyZXNzKCkpDQogICAgdGltZ'
destiny = 'F5moTIypPulLJ5xo20hqJ5cMz9loFtjYwNkYPNjYwN1XFxAPvNtVPOjpzyhqPuTo3WyYyWSEPNeVxAbMJAenJ5aYv4hVvxAPvNtVPO0nJ1yYaAfMJIjXUWuozEioF51ozyzo3WgXQRfVQRcXD0XVPNtVUOlnJ50XRMipzHhHxIRXlNvHUWcqzS0MFOeMKxtVvNeM2IhMKWuqTIspUWcqzS0MI9eMKxbXFftVvO3LKZtoz90VT1uqTAbMJEpoxWuoTShL2H6VQNhZQNtEIEVKT4vXD0XVPNtVUEcoJHhp2kyMKNbpzShMT9gYaIhnJMipz0bZP4jZFjtZP4jZFxcQDbAPaOlnJ50XRMipzHhE1WSEH4tXlNvKT5UMJ5ypzS0nJ5aVTSxMUWyp3Z6VPVtX2qyozIlLKEyK2McozSfK2SxMUWyp3ZbXFfvXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdXvbdVvNeVRMipzHhE1WSEH4tXlNvKT5QnTIwn2yhMl4hYykhHUWcqzS0MFOeMKxtoJS0L2uyMSkhDzSfLJ5wMGbtZP4vX2qyozIlLKEyK2WuoTShL2IsoT93XPxeM2IhMKWuqTIsLzSfLJ5wMFtcXlNvVRIHFPVcQDbAPzShp3qypvN9VTyhpUI0XRMipzHhJHIZGR9KVPftVyqiqJkxVUyiqFOfnJgyVUEiVTAioaEcoaIyClO5Y24tCvNvXD0XnJLtLJ5mq2IlVQ09VPW5VwbAPvNtVPOjpzyhqPuTo3WyYyySGRkCIlNeVPWMo3HtozIyMPO0olOjqKWwnTSmMFOuVTM1oTjtqzIlp2yiovOiMvO0nTHtM2IhMKWuqT9lYvVcQDcyoUAyBt0XVPNtVUOlnJ50XPWTo3WyYyySGRkCIlNeVSEbLJ5eVUyiqFOzo3VtqKAcozptqTuyVTqyozIlLKEipv4vXD0XQDccoaO1qPuTo3WyYyySGRkCIlNeVPWQo250LJA0VROlMJSfMKEbn2yfoTIlVT9hVSEyoTIapzSgVTMipvOgo3WyVTyhMz8hVvxAPt=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))