//
//  ViewController.swift
//  CheckLocale
//
//  Created by swuad_12 on 01/07/2019.
//  Copyright © 2019 swuad_12. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var localeLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        localeLabel.text = "언어 : \(Locale.preferredLanguages[0]) 지역 : \((Locale.current as NSLocale).object(forKey: .countryCode)!)"
    }

    
}

