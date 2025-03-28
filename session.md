## COOKIES
* We have to create cookies in `login()` function in views.py.
* And we can delete cookies in `logout()` function in views.py.



















{% extends "HUGLI-1/base.html" %}-->
<!--{% load static %}-->

<!--{% block content %}-->

<!--    &lt;!&ndash; Hero Section &ndash;&gt;-->
<!--    <section class="page-hero service-hero">-->
<!--      <h1>Pamohlets/Posters</h1>-->
<!--      <p>Demo text</p>-->
<!--    </section>-->

<!--    <main class="service-page-content">-->
<!--  -->
<!--      <section class="service-category">-->
<!--        <div class="container">-->
<!--            <div class="upload-container">-->
<!--                <h4 class="mb-3">Upload Your Image</h4>-->
<!--                <input type="file" id="imageUpload" class="form-control mb-3" accept="image/*">-->
<!--                <img id="preview" class="image-preview">-->
<!--                -->
<!--                <div class="row mt-3">-->
<!--                    <div class="col-md-6">-->
<!--                        <label for="widthInput" class="form-label">Width (px)</label>-->
<!--                        <input type="number" id="widthInput" class="form-control" placeholder="Enter width">-->
<!--                    </div>-->
<!--                    <div class="col-md-6">-->
<!--                        <label for="heightInput" class="form-label">Height (px)</label>-->
<!--                        <input type="number" id="heightInput" class="form-control" placeholder="Enter height">-->
<!--                    </div>-->
<!--                </div>-->
<!--        -->
<!--                <button class="btn btn-primary mt-3">Submit</button>-->
<!--            </div>-->
<!--        </div>-->
<!--        -->
<!--        <script>-->
<!--            document.getElementById("imageUpload").addEventListener("change", function(event) {-->
<!--                const file = event.target.files[0];-->
<!--                if (file) {-->
<!--                    const reader = new FileReader();-->
<!--                    reader.onload = function(e) {-->
<!--                        const img = document.getElementById("preview");-->
<!--                        img.src = e.target.result;-->
<!--                        img.style.display = "block";-->
<!--                    };-->
<!--                    reader.readAsDataURL(file);-->
<!--                }-->
<!--            });-->
<!--        </script>-->
<!--      </section>-->

<!--   -->
<!--    </main>-->

<!-- {% endblock %}