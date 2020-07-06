#### 模式（mode）
> 这个`mode`定义图像中像素的类型和深度。每个像素使用位深度的全范围。所以1位像素的范围是0-1，8位像素的范围是0-255等等。当前版本支持以下标准模式：
> ![image](15D32D15E9D4472C8574B17A6695E735)

#### PIL.Image
```python
from PIL import Image
```
| 属性     | 说明               |
| :------- | :----------------- |
| filename | 文件名             |
| format   | 格式               |
| mode     | 模式               |
| size     | (宽, 高)二元组     |
| width    | 宽                 |
| height   | 高                 |
| pelette  | 调色板，没有为None |
| info     | 相关数据字典       |

| 方法                                                         | 说明                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| Image.open(fp, mode='r')                                     | 打开                                                         |
| Image.merge(mode, bands)                                     | 单波合并为多波                                               |
| Image.new(mode, size, color=0)                               | 创建                                                         |
| Image.fromarray(obj, mode=None)                              | 导出数组接口的图像： `Image.fromarray(np.asarray(im))`       |
| im.show(title=None, command=None)                            | 显示                                                         |
| im.save(fp, format=None)                                     | 保存图像                                                     |
| im.rotate(angle, resample=0, expand=0, center=None, translate=None, fillcolor=None) | 逆时针旋转                                                   |
| im.thumbnail(size)                                           | 缩略图                                                       |
| im.convert(mode=None, matrix=None, dither=None, palette=0, color=256) | 转换                                                         |
| im.copy()                                                    | 复制                                                         |
| im.crop(box=None)                                            | 返回矩形区域                                                 |
| im.getbands()                                                | 返回区名称的元组                                             |
| im.getbbox()                                                 | 返回非零区域的边界框                                         |
| im.getextrema()                                              | 每个波段的最小最大像素值                                     |
| im.getpalette()                                              | 获取调色板，没有则显示[R,G,B,...]或无                        |
| im.getpixel(xy)                                              | 给定位置像素值                                               |
| im.histogram(mask=None, extrema=None)                        | 返回直方图                                                   |
| im.paste(im2, box=None)                                      | 粘贴图像（须匹配）                                           |
| im.point(lut, mode=None)                                     | 通过查找表或函数映射此图像                                   |
| im.putdata(data, scale=1.0, offset=0.0)                      | 将像素数据复制到此图像，像素=值*比例+偏移                    |
| im.putpixel(xy, value)                                       | 修改给定位置的像素                                           |
| im.resize(size, resample=3, box=None, reducing_gap=None)     | 更改图片大小                                                 |
| im.seek(frame)                                               | 查找图片给定帧（gif）                                        |
| im.tell()                                                    | 返回当前帧坐标                                               |
| im.split()                                                   | 拆分为单独带区                                               |
| im.getchannel(channel)                                       | 单个通道的图像（r,g,b为0,1,2）                               |
| im.transpose(method)                                         | 转置图像，method可为`PIL.Image.FLIP_LEFT_RIGHT`  `PIL.Image.FLIP_TOP_BOTTOM` `PIL.Image.ROTATE_90` `PIL.Image.ROTATE_180` `PIL.Image.ROTATE_270` `PIL.Image.TRANSPOSE` `PIL.Image.TRANSVERSE` |
| im.verify()                                                  | 验证图像                                                     |
| im.close()                                                   | 关闭文件指针                                                 |


#### PIL.ImageDraw
```python
from PIL import ImageDraw
```
`Draw(im, mode=None)` 创建可用于绘制给定图像的对象

| 方法                                                         | 说明               |
| :----------------------------------------------------------- | :----------------- |
| getfont()                                                    | 获取当前默认字体   |
| arc(xy, start, end, fill=None, width=0)                      | 绘制圆弧           |
| chord(xy, start, end, fill=None, outline=None, width=1)      | 绘制圆弧，直线连接 |
| ellipse(xy, fill=None, outline=None, width=1)                | 绘制椭圆           |
| line(xy, fill=None, width=0, joint=None)                     | 绘制线             |
| point(xy, fill=None)                                         | 绘制点             |
| polygon(xy, fill=None, outline=None)                         | 绘制多边形         |
| rectangle(xy, fill=None, outline=None, width=1)              | 绘制矩形           |
| text(xy, text, fill=None, font=None, anchor=None, spacing=4, align="left", direction=None, features=None, language=None, stroke_width=0, stroke_fill=None) | 绘制字符串         |
multiline_text(xy, text, fill=None, font=None, anchor=None, spacing=4, align="left", direction=None, features=None, language=None)


#### PIL.ImageFont
```python
from PIL import Image, ImageFont, ImageDraw

im = Image.new('RGB', (256, 256))
draw = ImageDraw(im)

# use a bitmap font
font = ImageFont.load("arial.pil")
draw.text((10, 10), "hello", font=font)

# use a truetype font
font = ImageFont.truetype("arial.ttf", 15)
draw.text((10, 15), "world", font=font)
```

| 方法                                                         | 说明                                    |
| :----------------------------------------------------------- | :-------------------------------------- |
| load(filename)                                               | 加载字体文件                            |
| load_default()                                               | 加载默认文件                            |
| truetype(font=None, size=10, index=0, encoding='', layout_engine=None) | 加载TrueType创建字体对象，如`arial.ttf` |
| font.getsize(text)                                           | 返回给定文本的宽度和高度                |