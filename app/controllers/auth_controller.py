# app/controllers/auth_controller.py
import os
from flask import Blueprint, current_app, jsonify, render_template, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash
from app.models.user_model import UserModel
from app import mysql 
from werkzeug.utils import secure_filename

auth_bp = Blueprint('auth', __name__, url_prefix='/admin')

# Set direktori upload gambar
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = UserModel.get_user_by_username(username)

        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            flash("Login berhasil!", "success")
            return redirect(url_for('auth.dashboard'))
        else:
            flash("Username atau password salah.", "error")  # Flash message untuk login gagal

    return render_template('login.html')
# app/controllers/auth_controller.py
@auth_bp.route('/dashboard')
def dashboard():
    cursor = mysql.connection.cursor()
    # Mengambil jumlah user
    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]
    
    # Mengambil jumlah artikel
    cursor.execute("SELECT COUNT(*) FROM articles")
    article_count = cursor.fetchone()[0]
    
    cursor.close()
    
    return render_template('dashboard.html', user_count=user_count, article_count=article_count)



# Daftar Users
@auth_bp.route('/users')
def users():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    return render_template('users.html', users=users)

# Tambah User
# app/controllers/auth_controller.py
from werkzeug.security import generate_password_hash, check_password_hash

# Route to add user (already hashing the password)
@auth_bp.route('/users/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Hash the password
        hashed_password = generate_password_hash(password)
        
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        mysql.connection.commit()
        cursor.close()
        
        flash('User berhasil ditambahkan!', 'success')
        return redirect(url_for('auth.users'))
    
    return render_template('add_user.html')

# Route to edit user
@auth_bp.route('/users/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    cursor = mysql.connection.cursor()
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if password:  # If a new password is provided
            # Hash the new password
            hashed_password = generate_password_hash(password)
            cursor.execute("UPDATE users SET username=%s, password=%s WHERE id=%s", (username, hashed_password, user_id))
        else:  # If no new password is provided, only update the username
            cursor.execute("UPDATE users SET username=%s WHERE id=%s", (username, user_id))
        
        mysql.connection.commit()
        cursor.close()
        
        flash('User berhasil diperbarui!', 'success')
        return redirect(url_for('auth.users'))
    
    # Fetch user data to prefill the form
    cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    
    return render_template('edit_user.html', user=user)


# Hapus User
@auth_bp.route('/users/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
    mysql.connection.commit()
    cursor.close()
    
    flash('User berhasil dihapus!', 'success')
    return redirect(url_for('auth.users'))

# Tambah Artikel
# Tambah Artikel

@auth_bp.route('/artikel')
def artikel():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM articles")
    articles = cursor.fetchall()
    cursor.close()
    return render_template('artikel.html', articles=articles)

# Route untuk menambah artikel
@auth_bp.route('/artikel/add', methods=['GET', 'POST'])
def add_artikel():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        image_filename = None
        # Proses upload gambar jika ada
        if 'image' in request.files:
            image = request.files['image']
            if image and allowed_file(image.filename):
                image_filename = secure_filename(image.filename)
                image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], image_filename))
                print("Image saved:", image_filename)  # Debugging

        # Simpan artikel ke database
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO articles (title, content, image) VALUES (%s, %s, %s)", (title, content, image_filename))
        mysql.connection.commit()
        cursor.close()
        
        flash('Artikel berhasil ditambahkan!', 'success')
        return redirect(url_for('auth.artikel'))
    
    return render_template('add_artikel.html')


# Edit Artikel
# Edit Artikel
@auth_bp.route('/artikel/edit/<int:artikel_id>', methods=['GET', 'POST'])
def edit_artikel(artikel_id):
    cursor = mysql.connection.cursor()
    
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        image_filename = None
        # Proses upload gambar jika ada
        if 'image' in request.files and request.files['image'].filename != '':
            image = request.files['image']
            if image and allowed_file(image.filename):
                image_filename = secure_filename(image.filename)
                image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], image_filename))

        # Ambil gambar yang lama jika tidak ada gambar baru
        if not image_filename:
            cursor.execute("SELECT image FROM articles WHERE id=%s", (artikel_id,))
            image_filename = cursor.fetchone()[0]
        
        # Update database
        cursor.execute("UPDATE articles SET title=%s, content=%s, image=%s WHERE id=%s", (title, content, image_filename, artikel_id))
        mysql.connection.commit()
        cursor.close()
        
        flash('Artikel berhasil diperbarui!', 'success')
        return redirect(url_for('auth.artikel'))
    
    cursor.execute("SELECT * FROM articles WHERE id=%s", (artikel_id,))
    artikel = cursor.fetchone()
    cursor.close()
    
    return render_template('edit_artikel.html', artikel=artikel)

# Daftar Artikel
# Hapus Artikel
@auth_bp.route('/artikel/delete/<int:artikel_id>', methods=['POST'])
def delete_artikel(artikel_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM articles WHERE id=%s", (artikel_id,))
    mysql.connection.commit()
    cursor.close()
    
    flash('Artikel berhasil dihapus!', 'success')
    return redirect(url_for('auth.artikel'))

# app/controllers/auth_controller.py
@auth_bp.route('/upload_image', methods=['POST'])
def upload_image():
    if 'upload' in request.files:
        image = request.files['upload']
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            image.save(filepath)
            url = url_for('static', filename='uploads/' + filename)
            return jsonify({"uploaded": True, "url": url})
    return jsonify({"uploaded": False, "error": {"message": "Gagal mengunggah gambar"}})

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("Anda telah logout.", "info")
    return redirect(url_for('auth.login'))
