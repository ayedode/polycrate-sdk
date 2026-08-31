from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_artifacts_create_actual_availability_error_component import (
        ApiV1ArtifactsCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifacts_create_annotations_error_component import (
        ApiV1ArtifactsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_artifacts_create_app_version_error_component import (
        ApiV1ArtifactsCreateAppVersionErrorComponent,
    )
    from ..models.api_v1_artifacts_create_archived_at_error_component import (
        ApiV1ArtifactsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_artifacts_create_archived_by_error_component import (
        ApiV1ArtifactsCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_artifacts_create_archived_error_component import ApiV1ArtifactsCreateArchivedErrorComponent
    from ..models.api_v1_artifacts_create_archived_reason_error_component import (
        ApiV1ArtifactsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_artifacts_create_changelog_error_component import ApiV1ArtifactsCreateChangelogErrorComponent
    from ..models.api_v1_artifacts_create_content_url_error_component import (
        ApiV1ArtifactsCreateContentUrlErrorComponent,
    )
    from ..models.api_v1_artifacts_create_created_by_component_error_component import (
        ApiV1ArtifactsCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_artifacts_create_created_by_user_error_component import (
        ApiV1ArtifactsCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_artifacts_create_criticality_error_component import (
        ApiV1ArtifactsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_artifacts_create_debug_mode_error_component import ApiV1ArtifactsCreateDebugModeErrorComponent
    from ..models.api_v1_artifacts_create_default_config_error_component import (
        ApiV1ArtifactsCreateDefaultConfigErrorComponent,
    )
    from ..models.api_v1_artifacts_create_deprecated_error_component import ApiV1ArtifactsCreateDeprecatedErrorComponent
    from ..models.api_v1_artifacts_create_description_error_component import (
        ApiV1ArtifactsCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_artifacts_create_digest_error_component import ApiV1ArtifactsCreateDigestErrorComponent
    from ..models.api_v1_artifacts_create_discovery_enabled_error_component import (
        ApiV1ArtifactsCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_artifacts_create_display_name_error_component import (
        ApiV1ArtifactsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_artifacts_create_kind_error_component import ApiV1ArtifactsCreateKindErrorComponent
    from ..models.api_v1_artifacts_create_labels_error_component import ApiV1ArtifactsCreateLabelsErrorComponent
    from ..models.api_v1_artifacts_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1ArtifactsCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_artifacts_create_license_error_component import ApiV1ArtifactsCreateLicenseErrorComponent
    from ..models.api_v1_artifacts_create_managed_by_content_type_error_component import (
        ApiV1ArtifactsCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_artifacts_create_managed_by_object_id_error_component import (
        ApiV1ArtifactsCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_artifacts_create_metadata_error_component import ApiV1ArtifactsCreateMetadataErrorComponent
    from ..models.api_v1_artifacts_create_mirrored_at_error_component import (
        ApiV1ArtifactsCreateMirroredAtErrorComponent,
    )
    from ..models.api_v1_artifacts_create_mirrored_content_url_error_component import (
        ApiV1ArtifactsCreateMirroredContentUrlErrorComponent,
    )
    from ..models.api_v1_artifacts_create_mirrored_error_component import ApiV1ArtifactsCreateMirroredErrorComponent
    from ..models.api_v1_artifacts_create_modified_by_user_error_component import (
        ApiV1ArtifactsCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_artifacts_create_name_error_component import ApiV1ArtifactsCreateNameErrorComponent
    from ..models.api_v1_artifacts_create_non_field_errors_error_component import (
        ApiV1ArtifactsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_artifacts_create_platform_dns_record_created_error_component import (
        ApiV1ArtifactsCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_artifacts_create_platform_service_error_component import (
        ApiV1ArtifactsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_artifacts_create_prerelease_error_component import ApiV1ArtifactsCreatePrereleaseErrorComponent
    from ..models.api_v1_artifacts_create_provider_error_component import ApiV1ArtifactsCreateProviderErrorComponent
    from ..models.api_v1_artifacts_create_provider_id_error_component import (
        ApiV1ArtifactsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_artifacts_create_provider_reference_error_component import (
        ApiV1ArtifactsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_artifacts_create_readme_md_error_component import ApiV1ArtifactsCreateReadmeMdErrorComponent
    from ..models.api_v1_artifacts_create_reconciliation_enabled_error_component import (
        ApiV1ArtifactsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_artifacts_create_scope_error_component import ApiV1ArtifactsCreateScopeErrorComponent
    from ..models.api_v1_artifacts_create_sla_availability_error_component import (
        ApiV1ArtifactsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifacts_create_sla_target_error_component import ApiV1ArtifactsCreateSlaTargetErrorComponent
    from ..models.api_v1_artifacts_create_sla_window_days_error_component import (
        ApiV1ArtifactsCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifacts_create_slo_availability_error_component import (
        ApiV1ArtifactsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifacts_create_slo_target_error_component import ApiV1ArtifactsCreateSloTargetErrorComponent
    from ..models.api_v1_artifacts_create_slo_window_days_error_component import (
        ApiV1ArtifactsCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifacts_create_source_urls_error_component import (
        ApiV1ArtifactsCreateSourceUrlsErrorComponent,
    )
    from ..models.api_v1_artifacts_create_spec_error_component import ApiV1ArtifactsCreateSpecErrorComponent
    from ..models.api_v1_artifacts_create_target_availability_error_component import (
        ApiV1ArtifactsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifacts_create_version_error_component import ApiV1ArtifactsCreateVersionErrorComponent
    from ..models.api_v1_artifacts_create_website_url_error_component import (
        ApiV1ArtifactsCreateWebsiteUrlErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ArtifactsCreateValidationError")


@_attrs_define
class ApiV1ArtifactsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ArtifactsCreateActualAvailabilityErrorComponent |
            ApiV1ArtifactsCreateAnnotationsErrorComponent | ApiV1ArtifactsCreateAppVersionErrorComponent |
            ApiV1ArtifactsCreateArchivedAtErrorComponent | ApiV1ArtifactsCreateArchivedByErrorComponent |
            ApiV1ArtifactsCreateArchivedErrorComponent | ApiV1ArtifactsCreateArchivedReasonErrorComponent |
            ApiV1ArtifactsCreateChangelogErrorComponent | ApiV1ArtifactsCreateContentUrlErrorComponent |
            ApiV1ArtifactsCreateCreatedByComponentErrorComponent | ApiV1ArtifactsCreateCreatedByUserErrorComponent |
            ApiV1ArtifactsCreateCriticalityErrorComponent | ApiV1ArtifactsCreateDebugModeErrorComponent |
            ApiV1ArtifactsCreateDefaultConfigErrorComponent | ApiV1ArtifactsCreateDeprecatedErrorComponent |
            ApiV1ArtifactsCreateDescriptionErrorComponent | ApiV1ArtifactsCreateDigestErrorComponent |
            ApiV1ArtifactsCreateDiscoveryEnabledErrorComponent | ApiV1ArtifactsCreateDisplayNameErrorComponent |
            ApiV1ArtifactsCreateKindErrorComponent | ApiV1ArtifactsCreateLabelsErrorComponent |
            ApiV1ArtifactsCreateLastReconciliationDurationSecondsErrorComponent | ApiV1ArtifactsCreateLicenseErrorComponent
            | ApiV1ArtifactsCreateManagedByContentTypeErrorComponent | ApiV1ArtifactsCreateManagedByObjectIdErrorComponent |
            ApiV1ArtifactsCreateMetadataErrorComponent | ApiV1ArtifactsCreateMirroredAtErrorComponent |
            ApiV1ArtifactsCreateMirroredContentUrlErrorComponent | ApiV1ArtifactsCreateMirroredErrorComponent |
            ApiV1ArtifactsCreateModifiedByUserErrorComponent | ApiV1ArtifactsCreateNameErrorComponent |
            ApiV1ArtifactsCreateNonFieldErrorsErrorComponent | ApiV1ArtifactsCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1ArtifactsCreatePlatformServiceErrorComponent | ApiV1ArtifactsCreatePrereleaseErrorComponent |
            ApiV1ArtifactsCreateProviderErrorComponent | ApiV1ArtifactsCreateProviderIdErrorComponent |
            ApiV1ArtifactsCreateProviderReferenceErrorComponent | ApiV1ArtifactsCreateReadmeMdErrorComponent |
            ApiV1ArtifactsCreateReconciliationEnabledErrorComponent | ApiV1ArtifactsCreateScopeErrorComponent |
            ApiV1ArtifactsCreateSlaAvailabilityErrorComponent | ApiV1ArtifactsCreateSlaTargetErrorComponent |
            ApiV1ArtifactsCreateSlaWindowDaysErrorComponent | ApiV1ArtifactsCreateSloAvailabilityErrorComponent |
            ApiV1ArtifactsCreateSloTargetErrorComponent | ApiV1ArtifactsCreateSloWindowDaysErrorComponent |
            ApiV1ArtifactsCreateSourceUrlsErrorComponent | ApiV1ArtifactsCreateSpecErrorComponent |
            ApiV1ArtifactsCreateTargetAvailabilityErrorComponent | ApiV1ArtifactsCreateVersionErrorComponent |
            ApiV1ArtifactsCreateWebsiteUrlErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ArtifactsCreateActualAvailabilityErrorComponent
        | ApiV1ArtifactsCreateAnnotationsErrorComponent
        | ApiV1ArtifactsCreateAppVersionErrorComponent
        | ApiV1ArtifactsCreateArchivedAtErrorComponent
        | ApiV1ArtifactsCreateArchivedByErrorComponent
        | ApiV1ArtifactsCreateArchivedErrorComponent
        | ApiV1ArtifactsCreateArchivedReasonErrorComponent
        | ApiV1ArtifactsCreateChangelogErrorComponent
        | ApiV1ArtifactsCreateContentUrlErrorComponent
        | ApiV1ArtifactsCreateCreatedByComponentErrorComponent
        | ApiV1ArtifactsCreateCreatedByUserErrorComponent
        | ApiV1ArtifactsCreateCriticalityErrorComponent
        | ApiV1ArtifactsCreateDebugModeErrorComponent
        | ApiV1ArtifactsCreateDefaultConfigErrorComponent
        | ApiV1ArtifactsCreateDeprecatedErrorComponent
        | ApiV1ArtifactsCreateDescriptionErrorComponent
        | ApiV1ArtifactsCreateDigestErrorComponent
        | ApiV1ArtifactsCreateDiscoveryEnabledErrorComponent
        | ApiV1ArtifactsCreateDisplayNameErrorComponent
        | ApiV1ArtifactsCreateKindErrorComponent
        | ApiV1ArtifactsCreateLabelsErrorComponent
        | ApiV1ArtifactsCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1ArtifactsCreateLicenseErrorComponent
        | ApiV1ArtifactsCreateManagedByContentTypeErrorComponent
        | ApiV1ArtifactsCreateManagedByObjectIdErrorComponent
        | ApiV1ArtifactsCreateMetadataErrorComponent
        | ApiV1ArtifactsCreateMirroredAtErrorComponent
        | ApiV1ArtifactsCreateMirroredContentUrlErrorComponent
        | ApiV1ArtifactsCreateMirroredErrorComponent
        | ApiV1ArtifactsCreateModifiedByUserErrorComponent
        | ApiV1ArtifactsCreateNameErrorComponent
        | ApiV1ArtifactsCreateNonFieldErrorsErrorComponent
        | ApiV1ArtifactsCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1ArtifactsCreatePlatformServiceErrorComponent
        | ApiV1ArtifactsCreatePrereleaseErrorComponent
        | ApiV1ArtifactsCreateProviderErrorComponent
        | ApiV1ArtifactsCreateProviderIdErrorComponent
        | ApiV1ArtifactsCreateProviderReferenceErrorComponent
        | ApiV1ArtifactsCreateReadmeMdErrorComponent
        | ApiV1ArtifactsCreateReconciliationEnabledErrorComponent
        | ApiV1ArtifactsCreateScopeErrorComponent
        | ApiV1ArtifactsCreateSlaAvailabilityErrorComponent
        | ApiV1ArtifactsCreateSlaTargetErrorComponent
        | ApiV1ArtifactsCreateSlaWindowDaysErrorComponent
        | ApiV1ArtifactsCreateSloAvailabilityErrorComponent
        | ApiV1ArtifactsCreateSloTargetErrorComponent
        | ApiV1ArtifactsCreateSloWindowDaysErrorComponent
        | ApiV1ArtifactsCreateSourceUrlsErrorComponent
        | ApiV1ArtifactsCreateSpecErrorComponent
        | ApiV1ArtifactsCreateTargetAvailabilityErrorComponent
        | ApiV1ArtifactsCreateVersionErrorComponent
        | ApiV1ArtifactsCreateWebsiteUrlErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_artifacts_create_actual_availability_error_component import (
            ApiV1ArtifactsCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_create_annotations_error_component import (
            ApiV1ArtifactsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_artifacts_create_app_version_error_component import (
            ApiV1ArtifactsCreateAppVersionErrorComponent,
        )
        from ..models.api_v1_artifacts_create_archived_at_error_component import (
            ApiV1ArtifactsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_artifacts_create_archived_by_error_component import (
            ApiV1ArtifactsCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_artifacts_create_archived_error_component import ApiV1ArtifactsCreateArchivedErrorComponent
        from ..models.api_v1_artifacts_create_archived_reason_error_component import (
            ApiV1ArtifactsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_artifacts_create_changelog_error_component import (
            ApiV1ArtifactsCreateChangelogErrorComponent,
        )
        from ..models.api_v1_artifacts_create_content_url_error_component import (
            ApiV1ArtifactsCreateContentUrlErrorComponent,
        )
        from ..models.api_v1_artifacts_create_created_by_component_error_component import (
            ApiV1ArtifactsCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_artifacts_create_criticality_error_component import (
            ApiV1ArtifactsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_artifacts_create_debug_mode_error_component import (
            ApiV1ArtifactsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_artifacts_create_default_config_error_component import (
            ApiV1ArtifactsCreateDefaultConfigErrorComponent,
        )
        from ..models.api_v1_artifacts_create_deprecated_error_component import (
            ApiV1ArtifactsCreateDeprecatedErrorComponent,
        )
        from ..models.api_v1_artifacts_create_description_error_component import (
            ApiV1ArtifactsCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_artifacts_create_digest_error_component import ApiV1ArtifactsCreateDigestErrorComponent
        from ..models.api_v1_artifacts_create_discovery_enabled_error_component import (
            ApiV1ArtifactsCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_artifacts_create_display_name_error_component import (
            ApiV1ArtifactsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_artifacts_create_kind_error_component import ApiV1ArtifactsCreateKindErrorComponent
        from ..models.api_v1_artifacts_create_labels_error_component import ApiV1ArtifactsCreateLabelsErrorComponent
        from ..models.api_v1_artifacts_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactsCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_artifacts_create_license_error_component import ApiV1ArtifactsCreateLicenseErrorComponent
        from ..models.api_v1_artifacts_create_managed_by_content_type_error_component import (
            ApiV1ArtifactsCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_artifacts_create_managed_by_object_id_error_component import (
            ApiV1ArtifactsCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_artifacts_create_metadata_error_component import ApiV1ArtifactsCreateMetadataErrorComponent
        from ..models.api_v1_artifacts_create_mirrored_at_error_component import (
            ApiV1ArtifactsCreateMirroredAtErrorComponent,
        )
        from ..models.api_v1_artifacts_create_mirrored_content_url_error_component import (
            ApiV1ArtifactsCreateMirroredContentUrlErrorComponent,
        )
        from ..models.api_v1_artifacts_create_mirrored_error_component import ApiV1ArtifactsCreateMirroredErrorComponent
        from ..models.api_v1_artifacts_create_modified_by_user_error_component import (
            ApiV1ArtifactsCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_artifacts_create_name_error_component import ApiV1ArtifactsCreateNameErrorComponent
        from ..models.api_v1_artifacts_create_non_field_errors_error_component import (
            ApiV1ArtifactsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_artifacts_create_platform_dns_record_created_error_component import (
            ApiV1ArtifactsCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_artifacts_create_platform_service_error_component import (
            ApiV1ArtifactsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_artifacts_create_prerelease_error_component import (
            ApiV1ArtifactsCreatePrereleaseErrorComponent,
        )
        from ..models.api_v1_artifacts_create_provider_error_component import ApiV1ArtifactsCreateProviderErrorComponent
        from ..models.api_v1_artifacts_create_provider_id_error_component import (
            ApiV1ArtifactsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_artifacts_create_provider_reference_error_component import (
            ApiV1ArtifactsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_artifacts_create_readme_md_error_component import (
            ApiV1ArtifactsCreateReadmeMdErrorComponent,
        )
        from ..models.api_v1_artifacts_create_reconciliation_enabled_error_component import (
            ApiV1ArtifactsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_artifacts_create_scope_error_component import ApiV1ArtifactsCreateScopeErrorComponent
        from ..models.api_v1_artifacts_create_sla_availability_error_component import (
            ApiV1ArtifactsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_create_sla_target_error_component import (
            ApiV1ArtifactsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_artifacts_create_sla_window_days_error_component import (
            ApiV1ArtifactsCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifacts_create_slo_availability_error_component import (
            ApiV1ArtifactsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_create_slo_target_error_component import (
            ApiV1ArtifactsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_artifacts_create_slo_window_days_error_component import (
            ApiV1ArtifactsCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifacts_create_source_urls_error_component import (
            ApiV1ArtifactsCreateSourceUrlsErrorComponent,
        )
        from ..models.api_v1_artifacts_create_spec_error_component import ApiV1ArtifactsCreateSpecErrorComponent
        from ..models.api_v1_artifacts_create_target_availability_error_component import (
            ApiV1ArtifactsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_create_version_error_component import ApiV1ArtifactsCreateVersionErrorComponent
        from ..models.api_v1_artifacts_create_website_url_error_component import (
            ApiV1ArtifactsCreateWebsiteUrlErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ArtifactsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateContentUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateWebsiteUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateSourceUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateAppVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateLicenseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateReadmeMdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateChangelogErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateDefaultConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateMirroredErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateMirroredContentUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateMirroredAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateDigestErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateDeprecatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreatePrereleaseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateMetadataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_artifacts_create_actual_availability_error_component import (
            ApiV1ArtifactsCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_create_annotations_error_component import (
            ApiV1ArtifactsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_artifacts_create_app_version_error_component import (
            ApiV1ArtifactsCreateAppVersionErrorComponent,
        )
        from ..models.api_v1_artifacts_create_archived_at_error_component import (
            ApiV1ArtifactsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_artifacts_create_archived_by_error_component import (
            ApiV1ArtifactsCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_artifacts_create_archived_error_component import ApiV1ArtifactsCreateArchivedErrorComponent
        from ..models.api_v1_artifacts_create_archived_reason_error_component import (
            ApiV1ArtifactsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_artifacts_create_changelog_error_component import (
            ApiV1ArtifactsCreateChangelogErrorComponent,
        )
        from ..models.api_v1_artifacts_create_content_url_error_component import (
            ApiV1ArtifactsCreateContentUrlErrorComponent,
        )
        from ..models.api_v1_artifacts_create_created_by_component_error_component import (
            ApiV1ArtifactsCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_artifacts_create_created_by_user_error_component import (
            ApiV1ArtifactsCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_artifacts_create_criticality_error_component import (
            ApiV1ArtifactsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_artifacts_create_debug_mode_error_component import (
            ApiV1ArtifactsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_artifacts_create_default_config_error_component import (
            ApiV1ArtifactsCreateDefaultConfigErrorComponent,
        )
        from ..models.api_v1_artifacts_create_deprecated_error_component import (
            ApiV1ArtifactsCreateDeprecatedErrorComponent,
        )
        from ..models.api_v1_artifacts_create_description_error_component import (
            ApiV1ArtifactsCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_artifacts_create_digest_error_component import ApiV1ArtifactsCreateDigestErrorComponent
        from ..models.api_v1_artifacts_create_discovery_enabled_error_component import (
            ApiV1ArtifactsCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_artifacts_create_display_name_error_component import (
            ApiV1ArtifactsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_artifacts_create_kind_error_component import ApiV1ArtifactsCreateKindErrorComponent
        from ..models.api_v1_artifacts_create_labels_error_component import ApiV1ArtifactsCreateLabelsErrorComponent
        from ..models.api_v1_artifacts_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactsCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_artifacts_create_license_error_component import ApiV1ArtifactsCreateLicenseErrorComponent
        from ..models.api_v1_artifacts_create_managed_by_content_type_error_component import (
            ApiV1ArtifactsCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_artifacts_create_managed_by_object_id_error_component import (
            ApiV1ArtifactsCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_artifacts_create_metadata_error_component import ApiV1ArtifactsCreateMetadataErrorComponent
        from ..models.api_v1_artifacts_create_mirrored_at_error_component import (
            ApiV1ArtifactsCreateMirroredAtErrorComponent,
        )
        from ..models.api_v1_artifacts_create_mirrored_content_url_error_component import (
            ApiV1ArtifactsCreateMirroredContentUrlErrorComponent,
        )
        from ..models.api_v1_artifacts_create_mirrored_error_component import ApiV1ArtifactsCreateMirroredErrorComponent
        from ..models.api_v1_artifacts_create_modified_by_user_error_component import (
            ApiV1ArtifactsCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_artifacts_create_name_error_component import ApiV1ArtifactsCreateNameErrorComponent
        from ..models.api_v1_artifacts_create_non_field_errors_error_component import (
            ApiV1ArtifactsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_artifacts_create_platform_dns_record_created_error_component import (
            ApiV1ArtifactsCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_artifacts_create_platform_service_error_component import (
            ApiV1ArtifactsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_artifacts_create_prerelease_error_component import (
            ApiV1ArtifactsCreatePrereleaseErrorComponent,
        )
        from ..models.api_v1_artifacts_create_provider_error_component import ApiV1ArtifactsCreateProviderErrorComponent
        from ..models.api_v1_artifacts_create_provider_id_error_component import (
            ApiV1ArtifactsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_artifacts_create_provider_reference_error_component import (
            ApiV1ArtifactsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_artifacts_create_readme_md_error_component import (
            ApiV1ArtifactsCreateReadmeMdErrorComponent,
        )
        from ..models.api_v1_artifacts_create_reconciliation_enabled_error_component import (
            ApiV1ArtifactsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_artifacts_create_scope_error_component import ApiV1ArtifactsCreateScopeErrorComponent
        from ..models.api_v1_artifacts_create_sla_availability_error_component import (
            ApiV1ArtifactsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_create_sla_target_error_component import (
            ApiV1ArtifactsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_artifacts_create_sla_window_days_error_component import (
            ApiV1ArtifactsCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifacts_create_slo_availability_error_component import (
            ApiV1ArtifactsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_create_slo_target_error_component import (
            ApiV1ArtifactsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_artifacts_create_slo_window_days_error_component import (
            ApiV1ArtifactsCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifacts_create_source_urls_error_component import (
            ApiV1ArtifactsCreateSourceUrlsErrorComponent,
        )
        from ..models.api_v1_artifacts_create_spec_error_component import ApiV1ArtifactsCreateSpecErrorComponent
        from ..models.api_v1_artifacts_create_target_availability_error_component import (
            ApiV1ArtifactsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_create_version_error_component import ApiV1ArtifactsCreateVersionErrorComponent
        from ..models.api_v1_artifacts_create_website_url_error_component import (
            ApiV1ArtifactsCreateWebsiteUrlErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ArtifactsCreateActualAvailabilityErrorComponent
                | ApiV1ArtifactsCreateAnnotationsErrorComponent
                | ApiV1ArtifactsCreateAppVersionErrorComponent
                | ApiV1ArtifactsCreateArchivedAtErrorComponent
                | ApiV1ArtifactsCreateArchivedByErrorComponent
                | ApiV1ArtifactsCreateArchivedErrorComponent
                | ApiV1ArtifactsCreateArchivedReasonErrorComponent
                | ApiV1ArtifactsCreateChangelogErrorComponent
                | ApiV1ArtifactsCreateContentUrlErrorComponent
                | ApiV1ArtifactsCreateCreatedByComponentErrorComponent
                | ApiV1ArtifactsCreateCreatedByUserErrorComponent
                | ApiV1ArtifactsCreateCriticalityErrorComponent
                | ApiV1ArtifactsCreateDebugModeErrorComponent
                | ApiV1ArtifactsCreateDefaultConfigErrorComponent
                | ApiV1ArtifactsCreateDeprecatedErrorComponent
                | ApiV1ArtifactsCreateDescriptionErrorComponent
                | ApiV1ArtifactsCreateDigestErrorComponent
                | ApiV1ArtifactsCreateDiscoveryEnabledErrorComponent
                | ApiV1ArtifactsCreateDisplayNameErrorComponent
                | ApiV1ArtifactsCreateKindErrorComponent
                | ApiV1ArtifactsCreateLabelsErrorComponent
                | ApiV1ArtifactsCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1ArtifactsCreateLicenseErrorComponent
                | ApiV1ArtifactsCreateManagedByContentTypeErrorComponent
                | ApiV1ArtifactsCreateManagedByObjectIdErrorComponent
                | ApiV1ArtifactsCreateMetadataErrorComponent
                | ApiV1ArtifactsCreateMirroredAtErrorComponent
                | ApiV1ArtifactsCreateMirroredContentUrlErrorComponent
                | ApiV1ArtifactsCreateMirroredErrorComponent
                | ApiV1ArtifactsCreateModifiedByUserErrorComponent
                | ApiV1ArtifactsCreateNameErrorComponent
                | ApiV1ArtifactsCreateNonFieldErrorsErrorComponent
                | ApiV1ArtifactsCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1ArtifactsCreatePlatformServiceErrorComponent
                | ApiV1ArtifactsCreatePrereleaseErrorComponent
                | ApiV1ArtifactsCreateProviderErrorComponent
                | ApiV1ArtifactsCreateProviderIdErrorComponent
                | ApiV1ArtifactsCreateProviderReferenceErrorComponent
                | ApiV1ArtifactsCreateReadmeMdErrorComponent
                | ApiV1ArtifactsCreateReconciliationEnabledErrorComponent
                | ApiV1ArtifactsCreateScopeErrorComponent
                | ApiV1ArtifactsCreateSlaAvailabilityErrorComponent
                | ApiV1ArtifactsCreateSlaTargetErrorComponent
                | ApiV1ArtifactsCreateSlaWindowDaysErrorComponent
                | ApiV1ArtifactsCreateSloAvailabilityErrorComponent
                | ApiV1ArtifactsCreateSloTargetErrorComponent
                | ApiV1ArtifactsCreateSloWindowDaysErrorComponent
                | ApiV1ArtifactsCreateSourceUrlsErrorComponent
                | ApiV1ArtifactsCreateSpecErrorComponent
                | ApiV1ArtifactsCreateTargetAvailabilityErrorComponent
                | ApiV1ArtifactsCreateVersionErrorComponent
                | ApiV1ArtifactsCreateWebsiteUrlErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_0 = (
                        ApiV1ArtifactsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_1 = (
                        ApiV1ArtifactsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_2 = (
                        ApiV1ArtifactsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_3 = (
                        ApiV1ArtifactsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_4 = (
                        ApiV1ArtifactsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_5 = (
                        ApiV1ArtifactsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_6 = (
                        ApiV1ArtifactsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_7 = (
                        ApiV1ArtifactsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_8 = (
                        ApiV1ArtifactsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_9 = (
                        ApiV1ArtifactsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_10 = (
                        ApiV1ArtifactsCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_11 = (
                        ApiV1ArtifactsCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_12 = (
                        ApiV1ArtifactsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_13 = (
                        ApiV1ArtifactsCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_14 = (
                        ApiV1ArtifactsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_15 = (
                        ApiV1ArtifactsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_16 = (
                        ApiV1ArtifactsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_17 = (
                        ApiV1ArtifactsCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_18 = (
                        ApiV1ArtifactsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_19 = (
                        ApiV1ArtifactsCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_20 = (
                        ApiV1ArtifactsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_21 = (
                        ApiV1ArtifactsCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_22 = (
                        ApiV1ArtifactsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_23 = (
                        ApiV1ArtifactsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_24 = (
                        ApiV1ArtifactsCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_25 = (
                        ApiV1ArtifactsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_26 = (
                        ApiV1ArtifactsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_27 = (
                        ApiV1ArtifactsCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_28 = (
                        ApiV1ArtifactsCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_29 = (
                        ApiV1ArtifactsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_30 = (
                        ApiV1ArtifactsCreateContentUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_31 = (
                        ApiV1ArtifactsCreateWebsiteUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_32 = (
                        ApiV1ArtifactsCreateSourceUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_33 = (
                        ApiV1ArtifactsCreateVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_34 = (
                        ApiV1ArtifactsCreateAppVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_35 = (
                        ApiV1ArtifactsCreateLicenseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_36 = (
                        ApiV1ArtifactsCreateReadmeMdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_37 = (
                        ApiV1ArtifactsCreateChangelogErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_38 = (
                        ApiV1ArtifactsCreateSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_39 = (
                        ApiV1ArtifactsCreateDefaultConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_40 = (
                        ApiV1ArtifactsCreateMirroredErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_41 = (
                        ApiV1ArtifactsCreateMirroredContentUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_42 = (
                        ApiV1ArtifactsCreateMirroredAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_43 = (
                        ApiV1ArtifactsCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_44 = (
                        ApiV1ArtifactsCreateDigestErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_45 = (
                        ApiV1ArtifactsCreateDeprecatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_46 = (
                        ApiV1ArtifactsCreatePrereleaseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_47 = (
                        ApiV1ArtifactsCreateMetadataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_48 = (
                        ApiV1ArtifactsCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_49 = (
                        ApiV1ArtifactsCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_create_error_type_50 = (
                        ApiV1ArtifactsCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_artifacts_create_error_type_51 = (
                    ApiV1ArtifactsCreateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_artifacts_create_error_type_51

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_artifacts_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_artifacts_create_validation_error.additional_properties = d
        return api_v1_artifacts_create_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
