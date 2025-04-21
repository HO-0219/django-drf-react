# serializers/resume_serializers.py

from rest_framework import serializers
from .models import Resume, Skill, Portfolio

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id', 'title', 'description', 'link']

class ResumeSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    portfolios = PortfolioSerializer(many=True)

    class Meta:
        model = Resume
        fields = ['id', 'title', 'summary', 'skills', 'portfolios', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data.pop('user', None)  # ✅ user 중복 방지

        skills_data = validated_data.pop('skills', [])
        portfolios_data = validated_data.pop('portfolios', [])
        resume = Resume.objects.create(user=user, **validated_data)


        for skill_data in skills_data:
            skill_obj, _ = Skill.objects.get_or_create(**skill_data)
            resume.skills.add(skill_obj)

        for port_data in portfolios_data:
            portfolio_obj = Portfolio.objects.create(**port_data)
            resume.portfolios.add(portfolio_obj)

        return resume

    def update(self, instance, validated_data):
        skills_data = validated_data.pop('skills', [])
        portfolios_data = validated_data.pop('portfolios', [])
        
        instance.title = validated_data.get('title', instance.title)
        instance.summary = validated_data.get('summary', instance.summary)
        instance.save()

        if skills_data:
            instance.skills.clear()
            for skill_data in skills_data:
                skill_obj, _ = Skill.objects.get_or_create(**skill_data)
                instance.skills.add(skill_obj)

        if portfolios_data:
            instance.portfolios.clear()
            for port_data in portfolios_data:
                #portfolio_obj = Portfolio.objects.create(**port_data)
                portfolio_obj, _ = Portfolio.objects.get_or_create(**port_data)

                instance.portfolios.add(portfolio_obj)

        return instance
