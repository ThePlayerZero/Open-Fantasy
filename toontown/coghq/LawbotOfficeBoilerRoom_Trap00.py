from toontown.coghq.SpecImports import *
GlobalEntities = {1000: {'type': 'levelMgr',
                         'name': 'LevelMgr',
                         'comment': '',
                         'parentEntId': 0,
                         'cogLevel': 0,
                         'farPlaneDistance': 1500,
                         'modelFilename': 'phase_10/models/cashbotHQ/ZONE08a',
                         'wantDoors': 1},
                  1001: {'type': 'editMgr',
                         'name': 'EditMgr',
                         'parentEntId': 0,
                         'insertEntity': None,
                         'removeEntity': None,
                         'requestNewEntity': None,
                         'requestSave': None},
                  0: {'type': 'zone',
                      'name': 'UberZone',
                      'comment': '',
                      'parentEntId': 0,
                      'scale': 1,
                      'description': '',
                      'visibility': []},
                  10055: {'type': 'attribModifier',
                          'name': '<unnamed>',
                          'comment': '',
                          'parentEntId': 10001,
                          'attribName': 'modelPath',
                          'recursive': 1,
                          'typeName': 'model',
                          'value': ''},
                  100023: {'type': 'goon',
                           'name': '<unnamed>',
                           'comment': '',
                           'parentEntId': 100022,
                           'pos': Point3(0, 0, 0),
                           'hpr': Vec3(0, 0, 0),
                           'scale': 3.5,
                           'attackRadius': 6.0,
                           'crushCellId': None,
                           'goonType': 'sg',
                           'gridId': None,
                           'hFov': 90.0,
                           'strength': 15,
                           'velocity': 4},
                  100000: {'type': 'model',
                           'name': 'wall',
                           'comment': '',
                           'parentEntId': 100004,
                           'pos': Point3(51.4205, -2.29817, 0),
                           'hpr': Vec3(0, 0, 0),
                           'scale': Point3(0.95, 2, 1.25),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'phase_10/models/lawbotHQ/LB_wall_panel.bam'},
                  100002: {'type': 'model',
                           'name': 'copy of wall',
                           'comment': '',
                           'parentEntId': 100004,
                           'pos': Point3(36.415, -2.3, 0),
                           'hpr': Vec3(0, 0, 0),
                           'scale': Point3(0.95, 2, 1.25),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'phase_10/models/lawbotHQ/LB_wall_panel.bam'},
                  100005: {'type': 'model',
                           'name': 'copy of wall (2)',
                           'comment': '',
                           'parentEntId': 100004,
                           'pos': Point3(23.2853, -0.371783, 0),
                           'hpr': Point3(90, 0, 0),
                           'scale': Point3(0.95, 2, 1.25),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'phase_10/models/lawbotHQ/LB_wall_panel.bam'},
                  100006: {'type': 'model',
                           'name': 'copy of wall (3)',
                           'comment': '',
                           'parentEntId': 100004,
                           'pos': Point3(23.2853, -15.2326, 0),
                           'hpr': Point3(90, 0, 0),
                           'scale': Point3(0.95, 2, 1.25),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'phase_10/models/lawbotHQ/LB_wall_panel.bam'},
                  100007: {'type': 'model',
                           'name': 'copy of wall (4)',
                           'comment': '',
                           'parentEntId': 100004,
                           'pos': Point3(23.2853, -30.3458, 0),
                           'hpr': Point3(90, 0, 0),
                           'scale': Point3(0.95, 2, 1.25),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'phase_10/models/lawbotHQ/LB_wall_panel.bam'},
                  100008: {'type': 'model',
                           'name': 'copy of wall (5)',
                           'comment': '',
                           'parentEntId': 100004,
                           'pos': Point3(8.38448, 29.6127, 0),
                           'hpr': Point3(90, 0, 0),
                           'scale': Point3(0.95, 2, 1.25),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'phase_10/models/lawbotHQ/LB_wall_panel.bam'},
                  100009: {'type': 'model',
                           'name': 'copy of wall (6)',
                           'comment': '',
                           'parentEntId': 100004,
                           'pos': Point3(8.38448, 14.8894, 0),
                           'hpr': Point3(90, 0, 0),
                           'scale': Point3(0.95, 2, 1.25),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'phase_10/models/lawbotHQ/LB_wall_panel.bam'},
                  100010: {'type': 'model',
                           'name': 'copy of wall (7)',
                           'comment': '',
                           'parentEntId': 100004,
                           'pos': Point3(8.38448, -0.135276, 0),
                           'hpr': Point3(90, 0, 0),
                           'scale': Point3(0.95, 2, 1.25),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'phase_10/models/lawbotHQ/LB_wall_panel.bam'},
                  100011: {'type': 'model',
                           'name': 'copy of wall (8)',
                           'comment': '',
                           'parentEntId': 100004,
                           'pos': Point3(-8.54444, 0.0828297, 0),
                           'hpr': Point3(0, 0, 0),
                           'scale': Point3(0.95, 2, 1.25),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'phase_10/models/lawbotHQ/LB_wall_panel.bam'},
                  100012: {'type': 'model',
                           'name': 'copy of wall (9)',
                           'comment': '',
                           'parentEntId': 100004,
                           'pos': Point3(-23.6854, 0.0828297, 0),
                           'hpr': Point3(0, 0, 0),
                           'scale': Point3(0.95, 2, 1.25),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'phase_10/models/lawbotHQ/LB_wall_panel.bam'},
                  100013: {'type': 'model',
                           'name': 'copy of wall (10)',
                           'comment': '',
                           'parentEntId': 100004,
                           'pos': Point3(-36.5, -45.2411, 0),
                           'hpr': Point3(90, 0, 0),
                           'scale': Point3(0.95, 2, 1.25),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'phase_10/models/lawbotHQ/LB_wall_panel.bam'},
                  100014: {'type': 'model',
                           'name': 'copy of wall (11)',
                           'comment': '',
                           'parentEntId': 100004,
                           'pos': Point3(-36.5, -30.557, 0),
                           'hpr': Point3(90, 0, 0),
                           'scale': Point3(0.95, 2, 1.25),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'phase_10/models/lawbotHQ/LB_wall_panel.bam'},
                  100015: {'type': 'model',
                           'name': 'copy of wall (12)',
                           'comment': '',
                           'parentEntId': 100004,
                           'pos': Point3(-36.5, -15.612, 0),
                           'hpr': Point3(90, 0, 0),
                           'scale': Point3(0.95, 2, 1.25),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'phase_10/models/lawbotHQ/LB_wall_panel.bam'},
                  100016: {'type': 'model',
                           'name': 'copy of wall (13)',
                           'comment': '',
                           'parentEntId': 100004,
                           'pos': Point3(-36.5, -0.453893, 0),
                           'hpr': Point3(90, 0, 0),
                           'scale': Point3(0.95, 2, 1.25),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'phase_10/models/lawbotHQ/LB_wall_panel.bam'},
                  100017: {'type': 'model',
                           'name': 'copy of wall (14)',
                           'comment': '',
                           'parentEntId': 100004,
                           'pos': Point3(-36.5, 14.6685, 0),
                           'hpr': Point3(90, 0, 0),
                           'scale': Point3(0.95, 2, 1.25),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'phase_10/models/lawbotHQ/LB_wall_panel.bam'},
                  100018: {'type': 'model',
                           'name': 'copy of wall (15)',
                           'comment': '',
                           'parentEntId': 100004,
                           'pos': Point3(-36.5, 14.6685, 0),
                           'hpr': Point3(0, 0, 0),
                           'scale': Point3(0.95, 2, 1.25),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'phase_10/models/lawbotHQ/LB_wall_panel.bam'},
                  100019: {'type': 'model',
                           'name': 'copy of wall (16)',
                           'comment': '',
                           'parentEntId': 100004,
                           'pos': Point3(-21.5858, 14.6685, 0),
                           'hpr': Point3(0, 0, 0),
                           'scale': Point3(0.95, 2, 1.25),
                           'collisionsOnly': 0,
                           'flattenType': 'light',
                           'loadType': 'loadModelCopy',
                           'modelPath': 'phase_10/models/lawbotHQ/LB_wall_panel.bam'},
                  10001: {'type': 'nodepath',
                          'name': 'crates',
                          'comment': '',
                          'parentEntId': 10028,
                          'pos': Point3(0, 0, 0),
                          'hpr': Vec3(0, 0, 0),
                          'scale': Vec3(1.3, 1.3, 1.64892)},
                  10002: {'type': 'nodepath',
                          'name': 'rewardBarrels',
                          'comment': '',
                          'parentEntId': 0,
                          'pos': Point3(-0.719734, 56.9691, 10.0021),
                          'hpr': Vec3(61.6992, 0, 0),
                          'scale': Vec3(1, 1, 1)},
                  10003: {'type': 'nodepath',
                          'name': 'upperWall',
                          'comment': 'TODO: replace with lines of shelves',
                          'parentEntId': 0,
                          'pos': Point3(-20.3203, 52.6549, 9.90873),
                          'hpr': Vec3(270, 0, 0),
                          'scale': Vec3(1.1143, 1.1143, 1.1143)},
                  10009: {'type': 'nodepath',
                          'name': 'toGear0',
                          'comment': '',
                          'parentEntId': 10001,
                          'pos': Point3(-26.5593, 31.856, 0),
                          'hpr': Vec3(0, 0, 0),
                          'scale': Vec3(1, 1, 1)},
                  10011: {'type': 'nodepath',
                          'name': 'toGear1',
                          'comment': '',
                          'parentEntId': 10001,
                          'pos': Point3(-25.884, 13.6749, 0),
                          'hpr': Vec3(41.6335, 0, 0),
                          'scale': Vec3(1, 1, 1)},
                  10023: {'type': 'nodepath',
                          'name': 'leftWall',
                          'comment': '',
                          'parentEntId': 10003,
                          'pos': Point3(0, 0, 0),
                          'hpr': Vec3(0, 0, 0),
                          'scale': 1},
                  10024: {'type': 'nodepath',
                          'name': 'rightWall',
                          'comment': '',
                          'parentEntId': 10003,
                          'pos': Point3(-26.7112, 6.85982, 0),
                          'hpr': Point3(180, 0, 0),
                          'scale': Vec3(1, 1, 1)},
                  10028: {'type': 'nodepath',
                          'name': 'lowerPuzzle',
                          'comment': '',
                          'parentEntId': 0,
                          'pos': Point3(0, 0, 0.05),
                          'hpr': Vec3(0, 0, 0),
                          'scale': 1},
                  10029: {'type': 'nodepath',
                          'name': 'entranceWall',
                          'comment': '',
                          'parentEntId': 10001,
                          'pos': Point3(0, 0, 0),
                          'hpr': Vec3(0, 0, 0),
                          'scale': 1},
                  10032: {'type': 'nodepath',
                          'name': 'props',
                          'comment': '',
                          'parentEntId': 0,
                          'pos': Point3(0, 0, 0),
                          'hpr': Vec3(0, 0, 0),
                          'scale': 1},
                  10038: {'type': 'nodepath',
                          'name': 'archStompers',
                          'comment': '',
                          'parentEntId': 10028,
                          'pos': Point3(0, 0, 0),
                          'hpr': Vec3(0, 0, 0),
                          'scale': 1},
                  10040: {'type': 'nodepath',
                          'name': 'backWall',
                          'comment': '',
                          'parentEntId': 10001,
                          'pos': Point3(0, 0, 0),
                          'hpr': Vec3(0, 0, 0),
                          'scale': 1},
                  10044: {'type': 'nodepath',
                          'name': 'gear',
                          'comment': '',
                          'parentEntId': 10028,
                          'pos': Point3(11.85, -11.38, 12.528),
                          'hpr': Vec3(0, 0, 0),
                          'scale': Vec3(1, 1, 1)},
                  10046: {'type': 'nodepath',
                          'name': 'supportedCrateBackWall',
                          'comment': '',
                          'parentEntId': 10028,
                          'pos': Point3(34.9045, -34.0589, -1.51687),
                          'hpr': Vec3(63.4349, 0, 0),
                          'scale': Vec3(1, 1, 1)},
                  10051: {'type': 'nodepath',
                          'name': 'supportedCrateEntrance',
                          'comment': '',
                          'parentEntId': 10028,
                          'pos': Point3(48.5077, 7.75915, 0.357897),
                          'hpr': Point3(0, 0, 0),
                          'scale': Vec3(1, 1, 1)},
                  10059: {'type': 'nodepath',
                          'name': 'largeStack',
                          'comment': '',
                          'parentEntId': 10029,
                          'pos': Point3(47.98, -16.98, 0),
                          'hpr': Vec3(0, 0, 0),
                          'scale': 1},
                  10061: {'type': 'nodepath',
                          'name': 'lower',
                          'comment': '',
                          'parentEntId': 10059,
                          'pos': Point3(0, 0, 0),
                          'hpr': Vec3(0, 0, 0),
                          'scale': 1},
                  100001: {'type': 'nodepath',
                           'name': 'trap1 cog node',
                           'comment': '',
                           'parentEntId': 0,
                           'pos': Point3(0, 0, 0),
                           'hpr': Vec3(0, 0, 0),
                           'scale': 1},
                  100004: {'type': 'nodepath',
                           'name': 'maze',
                           'comment': '',
                           'parentEntId': 0,
                           'pos': Point3(0, 0, 0),
                           'hpr': Vec3(0, 0, 0),
                           'scale': 1},
                  100021: {'type': 'nodepath',
                           'name': 'Goon Parent',
                           'comment': '',
                           'parentEntId': 0,
                           'pos': Point3(0, 0, 0),
                           'hpr': Vec3(0, 0, 0),
                           'scale': 1},
                  100003: {'type': 'path',
                           'name': 'test goon path',
                           'comment': '',
                           'parentEntId': 0,
                           'pos': Point3(-50.4808, 0, 0),
                           'hpr': Vec3(0, 0, 0),
                           'scale': Vec3(1, 1, 1),
                           'pathIndex': 0,
                           'pathScale': 1.0},
                  100020: {'type': 'path',
                           'name': 'GoonPath1',
                           'comment': '',
                           'parentEntId': 0,
                           'pos': Point3(0, 0, 0),
                           'hpr': Vec3(0, 0, 0),
                           'scale': 1,
                           'pathIndex': 0,
                           'pathScale': 1.0},
                  100022: {'type': 'path',
                           'name': 'GoonPath1',
                           'comment': '',
                           'parentEntId': 100021,
                           'pos': Point3(-10, -30, 0),
                           'hpr': Vec3(0, 0, 0),
                           'scale': Vec3(1, 1, 1),
                           'pathIndex': 0,
                           'pathScale': 2.0}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities,
             'scenarios': [Scenario0]}
