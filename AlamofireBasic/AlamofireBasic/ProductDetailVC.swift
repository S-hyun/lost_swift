//
//  ProductDetailVC.swift
//  AlamofireBasic
//
//  Created by swuad_12 on 12/07/2019.
//  Copyright © 2019 swuad_12. All rights reserved.
//

import UIKit
import Alamofire

class ProductDetailVC:UIViewController {
    var product_id:Int = 0
    var product_data :Product!
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        self.title  = "Product Detail\(product_id)"
        self.getProductDetail()
    }
    func getProductDetail() {
        guard let token = UserDefaults.standard.string(forKey: "token") else{
            print("토큰 없음")
            return
        }
        let headers:HTTPHeaders = [
            "Authorization":"Token \(token)",
            "Accept":"application/json"
        ]
        let url = "http://127.0.0.1:8000/shop/detail/"
        Alamofire.request(url, method: .get, headers: headers).responseData{
            response in
            switch response.result{
            case .failure:
                print("제품 목록 조회 오류")
            case .success:
                print("목록 조회 성공")
                guard let data = response.result.value else {
                    return
                }
                let decorder = JSONDecoder()
                do {
                    print(String(data:data, encoding: .utf8))
                    self.product_data = try decorder.decode(Product.self, from: data)
                } catch {
                    print(error)
                    print(error.localizedDescription)
                }
            }
        }
        
    }
    
}
