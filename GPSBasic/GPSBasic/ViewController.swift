//
//  ViewController.swift
//  GPSBasic
//
//  Created by swuad_12 on 09/07/2019.
//  Copyright © 2019 swuad_12. All rights reserved.
//

import UIKit
import CoreLocation
import MapKit

class ViewController: UIViewController, CLLocationManagerDelegate {

    @IBOutlet weak var mapView: MKMapView!
    
    var locationManager:CLLocationManager!
    var man:People!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        locationManager = CLLocationManager()
        locationManager.delegate = self
        locationManager.requestWhenInUseAuthorization()
        locationManager.desiredAccuracy = kCLLocationAccuracyBest
        locationManager.startUpdatingLocation()
        
        mapView.showsUserLocation = true
        setMapLocation(location: locationManager.location!)
    }
    
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        if let coor = manager.location?.coordinate {
            print("\(coor.latitude) \(coor.longitude)")
        }
        setMapLocation(location: manager.location!)
        // 바뀐 위치를 서버로 전송
    }

    func setMapLocation(location: CLLocation){
        // 서버에서 받아온 위치를 이용해서 지도 셋팅
        let regionRedius:CLLocationDistance = 100
        let coordinateRegion = MKCoordinateRegion(center: location.coordinate, latitudinalMeters: regionRedius, longitudinalMeters: regionRedius)
        mapView.setRegion(coordinateRegion, animated: false)
        if let annotation = self.man{
            self.man.coordinate = location.coordinate
        }
    }
    
    @IBAction func addAnnotation(_ sender: Any) {
        self.man = People(title: "Someone", coordinate: locationManager.location!.coordinate)
        mapView.addAnnotation(self.man)
    }
    
}

class People:NSObject, MKAnnotation{
    let title: String?
    var coordinate: CLLocationCoordinate2D
    
    init(title:String, coordinate:CLLocationCoordinate2D){
        self.title = title
        self.coordinate = coordinate
        super.init()
    }
}
