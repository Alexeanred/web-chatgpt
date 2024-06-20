document.addEventListener('DOMContentLoaded', function() {
    var generateCVButton = document.getElementById('generate-cv');
    var cvForm = document.getElementById('cv-form');
    var cvTemplates = document.querySelectorAll('input[name="template"]');
    var cvTemplateContainer = document.getElementById('cv-template');
    var cvPreviewContainer = document.getElementById('cv-preview');

    generateCVButton.addEventListener('click', function() {
        // Gather form data
        var name = document.getElementById('name').value;
        var email = document.getElementById('email').value;
        var phone = document.getElementById('phone').value;
        var education = document.getElementById('education').value;
        var experience = document.getElementById('experience').value;

        // Get selected template
        var selectedTemplate = document.querySelector('input[name="template"]:checked').value;

        // Generate CV based on selected template
        var cvContent = generateCVContent(name, email, phone, education, experience, selectedTemplate);

        // Display generated CV
        cvPreviewContainer.innerHTML = cvContent;

        // Show CV template container
        cvTemplateContainer.classList.remove('hidden');
    });

    function generateCVContent(name, email, phone, education, experience, template) {
        // Generate CV content based on selected template
        var content = '<p><strong>Name:</strong> ' + name + '</p>' +
                      '<p><strong>Email:</strong> ' + email + '</p>' +
                      '<p><strong>Phone:</strong> ' + phone + '</p>' +
                      '<p><strong>Education:</strong> ' + education + '</p>' +
                      '<p><strong>Experience:</strong> ' + experience + '</p>' +
                      '<p><strong>Template:</strong> ' + template + '</p>';
        
        return content;
    }
});
