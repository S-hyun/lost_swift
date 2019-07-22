//
//  ViewController.swift
//  TableTodo
//
//  Created by swuad_00 on 28/06/2019.
//  Copyright © 2019 swuad_00. All rights reserved.
//

import UIKit
import FMDB

class ViewController: UIViewController, UITableViewDataSource, UITextFieldDelegate {
    
    var todoData:[String] = []
    
    @IBOutlet weak var tableView: UITableView!
    @IBOutlet weak var btnSave: UIButton!
    @IBOutlet weak var textDoto: UITextField!
    
    var databasePath:String = ""
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        self.makeDB()
        self.todoLoad()
    }
    
    func makeDB() {
        let fileMgr = FileManager.default
        let dirPaths = NSSearchPathForDirectoriesInDomains(.documentDirectory, .userDomainMask, true)
        let docsDir = dirPaths[0]
        self.databasePath = docsDir + "/todo.db"
        
        // 만약 데이터베이스 파일이 없다면 신규 생성
        if !fileMgr.fileExists(atPath: self.databasePath) {
            // 데이터베이스 설정
            let db = FMDatabase(path: self.databasePath)
            
            if db.open() {
                let sql_query = "create table if not exists todo (id integer primary key autoincrement, todo text)"
                if !db.executeStatements(sql_query) {
                    NSLog("테이블 생성 오류")
                } else {
                    NSLog("테이블 생성 성공")
                }
                db.close()
            } else {
                NSLog("디비 연결 오류")
            }
        } else {
            NSLog("디비 있음")
        }
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return todoData.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "todoCell", for: indexPath) as! TodoCell
        let row = indexPath.row
        cell.index.text = "\(row+1)"
        cell.content.text = self.todoData[row]
        return cell
    }
    
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        textField.resignFirstResponder()
        
        self.todoData.append(self.textDoto.text!)
        self.textDoto.text = ""
        self.tableView.reloadData()
        return true
    }
    
    func todoLoad() {
        let db = FMDatabase(path: databasePath)
        if db.open() {
            let sql_query = "select * from todo"
            let result:FMResultSet? = db.executeQuery(sql_query, withArgumentsIn: [])
            if result != nil {
                while result!.next() {
                    self.todoData.append(result!.string(forColumn: "todo")!)
                }
            }
        }
    }
    
    @IBAction func todoSave(_ sender: UIButton) {
        self.textDoto.resignFirstResponder()
        var content_data = self.textDoto.text!
        self.todoData.append(content_data)
        self.textDoto.text = ""
        let db = FMDatabase(path: self.databasePath)
        if db.open() {
            db.executeStatements("delete from todo")
            if db.hadError() {
                NSLog("초기화 오류")
                return
            }
            
            for todo in self.todoData {
                let sql_query = "insert into todo (todo) values ('\(todo)')"
                do {
                    try db.executeUpdate(sql_query, values: nil)
                    NSLog("저장 성공")
                } catch {
                    NSLog("저장 오류")
               }
            }
        }
        
        self.tableView.reloadData()
    }
    
    func tableView(_ tableView: UITableView, canEditRowAt indexPath: IndexPath) -> Bool {
        return true
    }
    
    func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCell.EditingStyle, forRowAt indexPath: IndexPath) {
        if editingStyle == .delete {
            let row = indexPath.row
            self.todoData.remove(at: row)
            
            let db = FMDatabase(path: self.databasePath)
            if db.open() {
                db.executeStatements("delete from todo")
                if db.hadError() {
                    NSLog("초기화 오류")
                    return
                }
                
                for todo in self.todoData {
                    let sql_query = "insert into todo (todo) values ('\(todo)')"
                    do {
                        try db.executeUpdate(sql_query, values: nil)
                        NSLog("저장 성공")
                    } catch {
                        NSLog("저장 오류")
                    }
                }
            }
            
            tableView.reloadData()
        }
    }
    
}

