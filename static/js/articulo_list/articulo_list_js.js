const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.navbar ul');

hamburger.addEventListener('click', () => {
  hamburger.classList.toggle('active');
  navMenu.classList.toggle('active');
});

document.querySelectorAll('.navbar a').forEach(link => {
  link.addEventListener('click', () => {
    hamburger.classList.remove('active');
    navMenu.classList.remove('active');
  });
});

// Like functionality
document.querySelectorAll('.like-button').forEach(button => {
  button.addEventListener('click', function() {
    const likeCount = this.querySelector('.like-count');
    const currentLikes = parseInt(likeCount.textContent);
    
    if (!this.classList.contains('liked')) {
      likeCount.textContent = currentLikes + 1;
      this.classList.add('liked');
    } else {
      likeCount.textContent = currentLikes - 1;
      this.classList.remove('liked');
    }
    
    // Animate the like button
    this.style.transform = 'scale(0.9)';
    setTimeout(() => {
      this.style.transform = 'scale(1)';
    }, 100);
  });
});

// Article view functionality
const articleModal = document.getElementById('articleModal');
const closeArticleModal = document.getElementById('closeArticleModal');
const articleTitles = document.querySelectorAll('.blog-card h2');

// Function to open article modal
function openArticle(articleCard) {
  const title = articleCard.querySelector('h2').textContent;
  const meta = articleCard.querySelector('.meta').innerHTML;
  const likeButton = articleCard.querySelector('.like-button').cloneNode(true);
  
  articleModal.querySelector('.article-title').textContent = title;
  articleModal.querySelector('.article-meta').innerHTML = meta;
  
  // Get content without images and attachments sections
  const mainContent = articleCard.querySelector('.content p').innerHTML;
  articleModal.querySelector('.article-content').innerHTML = mainContent;
  
  // Handle images
  const articleMedia = articleModal.querySelector('.article-media');
  const images = articleCard.querySelectorAll('.post-images img');
  articleMedia.innerHTML = '';
  if(images.length > 0) {
    images.forEach(img => {
      const newImg = img.cloneNode(true);
      articleMedia.appendChild(newImg);
    });
    articleMedia.style.display = 'grid';
  } else {
    articleMedia.style.display = 'none';
  }
  
  // Handle attachments
  const attachmentsSection = articleModal.querySelector('.article-attachments');
  const attachments = articleCard.querySelector('.post-attachments');
  if(attachments) {
    attachmentsSection.innerHTML = `
      <h3 style="color: var(--primary); margin-bottom: 1rem;">Archivos adjuntos</h3>
      ${attachments.innerHTML}
    `;
    attachmentsSection.style.display = 'block';
  } else {
    attachmentsSection.style.display = 'none';
  }
  
  // Update interactions
  const interactionsDiv = articleModal.querySelector('.article-interactions');
  interactionsDiv.innerHTML = '';
  interactionsDiv.appendChild(likeButton);
  
  // Add click handler to the cloned like button
  likeButton.addEventListener('click', function() {
    const likeCount = this.querySelector('.like-count');
    const currentLikes = parseInt(likeCount.textContent);
    
    if (!this.classList.contains('liked')) {
      likeCount.textContent = currentLikes + 1;
      this.classList.add('liked');
    } else {
      likeCount.textContent = currentLikes - 1;
      this.classList.remove('liked');
    }
    
    // Update the original article's like count
    const originalLikeCount = articleCard.querySelector('.like-count');
    originalLikeCount.textContent = likeCount.textContent;
    if (this.classList.contains('liked')) {
      articleCard.querySelector('.like-button').classList.add('liked');
    } else {
      articleCard.querySelector('.like-button').classList.remove('liked');
    }
  });
  
  articleModal.classList.add('active');
}

// Add click handlers to article titles
articleTitles.forEach(title => {
  title.style.cursor = 'pointer';
  title.addEventListener('click', () => {
    const articleCard = title.closest('.blog-card');
    openArticle(articleCard);
  });
});

// Close article modal
closeArticleModal.addEventListener('click', () => {
  articleModal.classList.remove('active');
});

articleModal.addEventListener('click', (e) => {
  if (e.target === articleModal) {
    articleModal.classList.remove('active');
  }
});

// New JavaScript for create post functionality
const createPostBtn = document.getElementById('createPostBtn');
const modal = document.getElementById('createPostModal');
const closeModal = document.getElementById('closeModal');
const postForm = document.getElementById('postForm');

createPostBtn.addEventListener('click', () => {
  modal.classList.add('active');
});

closeModal.addEventListener('click', () => {
  modal.classList.remove('active');
});

modal.addEventListener('click', (e) => {
  if (e.target === modal) {
    modal.classList.remove('active');
  }
});

const imageInput = document.getElementById('images');
const attachmentsInput = document.getElementById('attachments');
const imagePreview = document.getElementById('imagePreview');
const fileList = document.getElementById('fileList');

imageInput.addEventListener('change', function(e) {
  imagePreview.innerHTML = '';
  const files = Array.from(e.target.files);
  
  files.forEach(file => {
    if (file.type.startsWith('image/')) {
      const reader = new FileReader();
      reader.onload = function(e) {
        const img = document.createElement('img');
        img.src = e.target.result;
        img.className = 'preview-image';
        imagePreview.appendChild(img);
      }
      reader.readAsDataURL(file);
    }
  });
});

attachmentsInput.addEventListener('change', function(e) {
  fileList.innerHTML = '';
  const files = Array.from(e.target.files);
  
  files.forEach(file => {
    const fileItem = document.createElement('div');
    fileItem.className = 'file-item';
    fileItem.innerHTML = `
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor">
        <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"></path>
        <polyline points="13 2 13 9 20 9"></polyline>
      </svg>
      <span>${file.name}</span>
      <span class="remove-file">×</span>
    `;
    
    fileList.appendChild(fileItem);
  });
});

// Update the form submission handler to include files
postForm.addEventListener('submit', (e) => {
  e.preventDefault();
  
  const formData = new FormData(postForm);
  const title = formData.get('title');
  const author = formData.get('author');
  const content = formData.get('content');
  const images = formData.getAll('images');
  const attachments = formData.getAll('attachments');
  
  const blogGrid = document.querySelector('.blog-grid');
  const newPost = document.createElement('article');
  newPost.className = 'blog-card';
  
  const currentDate = new Date().toLocaleDateString('es-ES', {
    day: 'numeric',
    month: 'short',
    year: 'numeric'
  });
  
  // Create image preview HTML if there are images
  let imageHTML = '';
  if (images.length > 0) {
    imageHTML = '<div class="post-images" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem; margin: 1rem 0;">';
    Array.from(images).forEach(image => {
      const url = URL.createObjectURL(image);
      imageHTML += `<img src="${url}" alt="Uploaded image" style="width: 100%; height: 150px; object-fit: cover; border-radius: 8px; border: 2px solid var(--primary);">`;
    });
    imageHTML += '</div>';
  }
  
  // Create attachments list HTML if there are attachments
  let attachmentsHTML = '';
  if (attachments.length > 0) {
    attachmentsHTML = `
      <div class="post-attachments" style="background: rgba(0,255,0,0.1); padding: 1rem; border-radius: 8px; margin-top: 1rem;">
        <h4 style="color: var(--primary); margin-bottom: 0.5rem;">Archivos adjuntos:</h4>
    `;
    Array.from(attachments).forEach(file => {
      attachmentsHTML += `
        <div class="file-item" style="display: flex; align-items: center; gap: 0.5rem; padding: 0.5rem; background: rgba(0,0,0,0.3); border-radius: 5px; margin-bottom: 0.5rem;">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"></path>
            <polyline points="13 2 13 9 20 9"></polyline>
          </svg>
          <span>${file.name}</span>
        </div>
      `;
    });
    attachmentsHTML += '</div>';
  }
  
  newPost.innerHTML = `
    <h2>${title}</h2>
    <div class="meta">
      <span>Por: ${author}</span>
      <span>${currentDate}</span>
    </div>
    <div class="content">
      <p>${content}</p>
      ${imageHTML}
      ${attachmentsHTML}
    </div>
    <button class="like-button" data-post-id="${Date.now()}">
      <span class="like-icon">♥</span>
      <span class="like-count">0</span>
    </button>
  `;
  
  blogGrid.insertBefore(newPost, blogGrid.firstChild);
  modal.classList.remove('active');
  postForm.reset();
  imagePreview.innerHTML = '';
  fileList.innerHTML = '';
  
  const newLikeButton = newPost.querySelector('.like-button');
  newLikeButton.addEventListener('click', handleLike);
  
  const newTitle = newPost.querySelector('h2');
  newTitle.style.cursor = 'pointer';
  newTitle.addEventListener('click', () => {
    openArticle(newPost);
  });
});

// Animate blog cards on scroll
const cards = document.querySelectorAll('.blog-card');
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
    }
  });
}, {
  threshold: 0.1
});

cards.forEach(card => {
  card.style.opacity = '0';
  card.style.transform = 'translateY(50px)';
  card.style.transition = 'all 0.5s ease-out';
  observer.observe(card);
});
