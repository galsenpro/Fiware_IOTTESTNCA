{
	"datamodels" : {
		"entities" : [{
			"context" : "SORTIES",
			"datamodel" : [{
					    "id": " Beach-A-Concha-123456 ",
					    "type": "Beach",
					    "name": "Playa de a Concha",
					    "description": "La Playa de A Concha se presenta .....",
					    "address": {
							    "addressCountry": "ES",
						        "addressLocality": "Vilagarcía de Arousa"
						    },
						"beachType": ["whiteSand", "urban", "calmWaters"],
						"occupationRate": "high",
						"facilities": ["promenade", "showers", "cleaningServices", "lifeGuard"],
						"accessType": ["privateVehicle", "onFoot", "publicTransport"],
						"location": {
							   "type": "Point",
							   "coordinates": [-8.768460000000001, 42.60214472222222]
							},
						"width": 51,
						"length": 450,
						"source": "http://www.tourspain.es"
					},{
					    "id": "Santander-Garden-Piquio",
					    "type": "Garden",
					    "name": "Jardines de Piquio",
					    "description": "Jardines de Piquio. Zona El Sardinero",
					    "location": {
						        "type": "Point",
						    	"coordinates": [-3.7836974, 43.4741091]
					        },
					    "address": {
						       "streetAddress": "Avenida Castañeda",
						       "addressLocality": "Santander",
						       "postalCode": "39005"
					        },
					    "openingHours": "Mo-Su",
					    "style": "french",
					    "category": ["public"],
					    "areaServed": "El Sardinero",
					    "dateLastWatering": "2017-03-31T:08:00",
					    "refRecord": ["Santander-Garden-Piquio-Record-1"]
				    },{
					    "id": "PointOfInterest-A-Concha-123456",
					    "type": "PointOfInterest",
					    "name": "Playa de a Concha",
					    "description": "La Playa de A Concha se presenta como una continuación de la Playa de Compostela, una de las más frecuentadas de Vilagarcía.",
					    "address": {
						      "addressCountry": "ES",
						      "addressLocality": "Vilagarcía de Arousa"
					    },
					    "category": ["113"],
					    "location": {
						      "type": "Point",
						      "coordinates": [
							        -8.768460000000001, 42.60214472222222
					      ]
					    },
					    "source": "http://www.tourspain.es",
					    "refSeeAlso": ["Beach-A-Concha-123456"]
					},{
					    "id": "Museum-Barcelona-MACBA-1234",
					    "type": "Museum",
					    "name": "Museo de Arte Contemporaneo de Barcelona",
					    "alternateName": "MACBA",
					    "description": "The MACBA was designed by the American architect Richard Meier and inaugurated in 1995.",
					    "address": {
						       "addressCountry": "ES",
						       "addressLocality": "Barcelona",
						       "streetAddress": "Plaza Dels Àngels, 1"
					    },
					    "museumType": ["fineArts"],
					    "artPeriod": ["contemporary"],
					    "facilities": ["shop", "cloakRoom", "guidedTour"],
					    "location": {
					       "type": "Point",
					       "coordinates": [ 2.1668771521199393, 41.38302235796602]
					    },
					    "openingHoursSpecification": [
					       {
					           "opens":  "11:00",
					           "closes": "19:30",
					           "dayOfWeek": "Mo, Wed, Thu, Fr"
					       },
					       {
					           "opens": "10:00",
					           "closes": "21:00",
					           "dayOfWeek": "Sat"
					       },
					       {
					           "opens": "10:00",
					           "closes": "15:00",
					           "dayOfWeek": "Sun"
					       }],
					    "touristArea": "Barcelona-Capital",
					    "source": "http://www.tourspain.es"
					}]},#Fin des datamodels de SORTIES
			{"context" : "TRANSPORTS",
			"datamodel" : [{
				        "id": "Spain-Road-A62",
				        "type": "Road",
				        "name": "A-62",
				        "alternateName": "E-80",
				        "description": "Autovía de Castilla",
				        "roadClass": "motorway",
				        "length": 355,
				        "refRoadSegment": ["Spain-RoadSegment-A62-0-355-forwards", "Spain-RoadSegment-A62-0-355-backwards"],
				        "responsible": "Ministerio de Fomento - Gobierno de España"
				    },{
					    "id": "Spain-RoadSegment-A62-osm-24702186",
					    "type": "RoadSegment",
					    "name": "Valladolid-Dueñas",
					    "category": ["oneway"],
					    "refRoad": "Spain-Road-A62",
					    "totalLaneNumber": 2,
					    "maximumAllowedSpeed": 120,
					    "minimumAllowedSpeed": 60,
					    "startPoint": {
						      "type": "Point",
						      "coordinates": [-4.7299180606009, 41.6844918725019]
					    },
					    "endPoint": {
					      		"type": "Point",
					      		"coordinates": [-4.55167335377909, 41.8570461783071]
					    },
					    "allowedVehicleType": [
					        	"car", "bus", "lorry", "trailer",
					        	"tanker", "van", "caravan"
					    ],
					    "location": {
					       "type": "LineString",
					       "coordinates": [
					            [
					               -4.7299180606009, 41.6844918725019
					            ],
					            [
					              -4.72855890957602, 41.6860596957855
					            ],
					            [
					              -4.5520357341647, 41.8569278186523
					            ],
					            [
					               -4.55167335377909, 41.8570461783071
					            ]
					       ]
					    },
					    "laneUsage": ["forward", "forward"],
					    "source": "http://wwww.openstreetmap.org"
					},{
						"id": "vehicle:WasteManagement:1",
						"type": "Vehicle",
						"vehicleType": "lorry",
						"category": ["municipalServices"],
						"location": {
						    	"type": "Point",
						    	"coordinates": [ -3.164485591715449, 40.62785133667262 ]
						  	},
						"name": "C Recogida 1",
						"speed": 50,
						"cargoWeight": 314,
						"serviceStatus": "onRoute, garbageCollection",
						"serviceProvided": ["gargabeCollection", "wasteContainerCleaning"],
						"areaServed": "Centro",
						"refVehicleModel": "vehiclemodel:econic",
						"vehiclePlateIdentifier": "3456ABC"
					}]},
				{
				"context" : "HEBERGEMENT"
					},{
					"context" : "PUBLIC",
					"datamodel" : [{
					     "id": "Museum-Barcelona-MACBA-1234",
					     "type": "Museum",
					     "name": "Museo de Arte Contemporaneo de Barcelona",
					     "alternateName": "MACBA",
					     "description": "The MACBA was designed by the American architect Richard Meier and inaugurated in 1995.",
					     "address": {
						        "addressCountry": "ES",
						        "addressLocality": "Barcelona",
						        "streetAddress": "Plaza Dels Àngels, 1"
					     },
					     "museumType": ["fineArts"],
					     "artPeriod": ["contemporary"],
					     "facilities": ["shop", "cloakRoom", "guidedTour"],
					     "location": {
						        "type": "Point",
						        "coordinates": [ 2.1668771521199393, 41.38302235796602]
					     },
					     "openingHoursSpecification": [
					        {
						            "opens":  "11:00",
						            "closes": "19:30",
						            "dayOfWeek": "Mo, Wed, Thu, Fr"
					        },
					        {
					            "opens": "10:00",
					            "closes": "21:00",
					            "dayOfWeek": "Sat"
					        },
					        {
					            "opens": "10:00",
					            "closes": "15:00",
					            "dayOfWeek": "Sun"
					        }
					    ],
					    "touristArea": "Barcelona-Capital",
					    "source": "http://www.tourspain.es"
					}]}
					]
		
	}
}