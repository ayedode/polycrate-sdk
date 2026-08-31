from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_artifacts_archive_create_actual_availability_error_component import (
        ApiV1ArtifactsArchiveCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_annotations_error_component import (
        ApiV1ArtifactsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_app_version_error_component import (
        ApiV1ArtifactsArchiveCreateAppVersionErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_archived_at_error_component import (
        ApiV1ArtifactsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_archived_by_error_component import (
        ApiV1ArtifactsArchiveCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_archived_error_component import (
        ApiV1ArtifactsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_archived_reason_error_component import (
        ApiV1ArtifactsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_changelog_error_component import (
        ApiV1ArtifactsArchiveCreateChangelogErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_content_url_error_component import (
        ApiV1ArtifactsArchiveCreateContentUrlErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_created_by_component_error_component import (
        ApiV1ArtifactsArchiveCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_created_by_user_error_component import (
        ApiV1ArtifactsArchiveCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_criticality_error_component import (
        ApiV1ArtifactsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_debug_mode_error_component import (
        ApiV1ArtifactsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_default_config_error_component import (
        ApiV1ArtifactsArchiveCreateDefaultConfigErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_deprecated_error_component import (
        ApiV1ArtifactsArchiveCreateDeprecatedErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_description_error_component import (
        ApiV1ArtifactsArchiveCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_digest_error_component import (
        ApiV1ArtifactsArchiveCreateDigestErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_discovery_enabled_error_component import (
        ApiV1ArtifactsArchiveCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_display_name_error_component import (
        ApiV1ArtifactsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_kind_error_component import (
        ApiV1ArtifactsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_labels_error_component import (
        ApiV1ArtifactsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1ArtifactsArchiveCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_license_error_component import (
        ApiV1ArtifactsArchiveCreateLicenseErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_managed_by_content_type_error_component import (
        ApiV1ArtifactsArchiveCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_managed_by_object_id_error_component import (
        ApiV1ArtifactsArchiveCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_metadata_error_component import (
        ApiV1ArtifactsArchiveCreateMetadataErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_mirrored_at_error_component import (
        ApiV1ArtifactsArchiveCreateMirroredAtErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_mirrored_content_url_error_component import (
        ApiV1ArtifactsArchiveCreateMirroredContentUrlErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_mirrored_error_component import (
        ApiV1ArtifactsArchiveCreateMirroredErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_modified_by_user_error_component import (
        ApiV1ArtifactsArchiveCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_name_error_component import (
        ApiV1ArtifactsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_non_field_errors_error_component import (
        ApiV1ArtifactsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_platform_dns_record_created_error_component import (
        ApiV1ArtifactsArchiveCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_platform_service_error_component import (
        ApiV1ArtifactsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_prerelease_error_component import (
        ApiV1ArtifactsArchiveCreatePrereleaseErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_provider_error_component import (
        ApiV1ArtifactsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_provider_id_error_component import (
        ApiV1ArtifactsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_provider_reference_error_component import (
        ApiV1ArtifactsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_readme_md_error_component import (
        ApiV1ArtifactsArchiveCreateReadmeMdErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_reconciliation_enabled_error_component import (
        ApiV1ArtifactsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_scope_error_component import (
        ApiV1ArtifactsArchiveCreateScopeErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_sla_availability_error_component import (
        ApiV1ArtifactsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_sla_target_error_component import (
        ApiV1ArtifactsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_sla_window_days_error_component import (
        ApiV1ArtifactsArchiveCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_slo_availability_error_component import (
        ApiV1ArtifactsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_slo_target_error_component import (
        ApiV1ArtifactsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_slo_window_days_error_component import (
        ApiV1ArtifactsArchiveCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_source_urls_error_component import (
        ApiV1ArtifactsArchiveCreateSourceUrlsErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_spec_error_component import (
        ApiV1ArtifactsArchiveCreateSpecErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_target_availability_error_component import (
        ApiV1ArtifactsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_version_error_component import (
        ApiV1ArtifactsArchiveCreateVersionErrorComponent,
    )
    from ..models.api_v1_artifacts_archive_create_website_url_error_component import (
        ApiV1ArtifactsArchiveCreateWebsiteUrlErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ArtifactsArchiveCreateValidationError")


@_attrs_define
class ApiV1ArtifactsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ArtifactsArchiveCreateActualAvailabilityErrorComponent |
            ApiV1ArtifactsArchiveCreateAnnotationsErrorComponent | ApiV1ArtifactsArchiveCreateAppVersionErrorComponent |
            ApiV1ArtifactsArchiveCreateArchivedAtErrorComponent | ApiV1ArtifactsArchiveCreateArchivedByErrorComponent |
            ApiV1ArtifactsArchiveCreateArchivedErrorComponent | ApiV1ArtifactsArchiveCreateArchivedReasonErrorComponent |
            ApiV1ArtifactsArchiveCreateChangelogErrorComponent | ApiV1ArtifactsArchiveCreateContentUrlErrorComponent |
            ApiV1ArtifactsArchiveCreateCreatedByComponentErrorComponent |
            ApiV1ArtifactsArchiveCreateCreatedByUserErrorComponent | ApiV1ArtifactsArchiveCreateCriticalityErrorComponent |
            ApiV1ArtifactsArchiveCreateDebugModeErrorComponent | ApiV1ArtifactsArchiveCreateDefaultConfigErrorComponent |
            ApiV1ArtifactsArchiveCreateDeprecatedErrorComponent | ApiV1ArtifactsArchiveCreateDescriptionErrorComponent |
            ApiV1ArtifactsArchiveCreateDigestErrorComponent | ApiV1ArtifactsArchiveCreateDiscoveryEnabledErrorComponent |
            ApiV1ArtifactsArchiveCreateDisplayNameErrorComponent | ApiV1ArtifactsArchiveCreateKindErrorComponent |
            ApiV1ArtifactsArchiveCreateLabelsErrorComponent |
            ApiV1ArtifactsArchiveCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1ArtifactsArchiveCreateLicenseErrorComponent | ApiV1ArtifactsArchiveCreateManagedByContentTypeErrorComponent
            | ApiV1ArtifactsArchiveCreateManagedByObjectIdErrorComponent | ApiV1ArtifactsArchiveCreateMetadataErrorComponent
            | ApiV1ArtifactsArchiveCreateMirroredAtErrorComponent |
            ApiV1ArtifactsArchiveCreateMirroredContentUrlErrorComponent | ApiV1ArtifactsArchiveCreateMirroredErrorComponent
            | ApiV1ArtifactsArchiveCreateModifiedByUserErrorComponent | ApiV1ArtifactsArchiveCreateNameErrorComponent |
            ApiV1ArtifactsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1ArtifactsArchiveCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1ArtifactsArchiveCreatePlatformServiceErrorComponent | ApiV1ArtifactsArchiveCreatePrereleaseErrorComponent |
            ApiV1ArtifactsArchiveCreateProviderErrorComponent | ApiV1ArtifactsArchiveCreateProviderIdErrorComponent |
            ApiV1ArtifactsArchiveCreateProviderReferenceErrorComponent | ApiV1ArtifactsArchiveCreateReadmeMdErrorComponent |
            ApiV1ArtifactsArchiveCreateReconciliationEnabledErrorComponent | ApiV1ArtifactsArchiveCreateScopeErrorComponent
            | ApiV1ArtifactsArchiveCreateSlaAvailabilityErrorComponent | ApiV1ArtifactsArchiveCreateSlaTargetErrorComponent
            | ApiV1ArtifactsArchiveCreateSlaWindowDaysErrorComponent |
            ApiV1ArtifactsArchiveCreateSloAvailabilityErrorComponent | ApiV1ArtifactsArchiveCreateSloTargetErrorComponent |
            ApiV1ArtifactsArchiveCreateSloWindowDaysErrorComponent | ApiV1ArtifactsArchiveCreateSourceUrlsErrorComponent |
            ApiV1ArtifactsArchiveCreateSpecErrorComponent | ApiV1ArtifactsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1ArtifactsArchiveCreateVersionErrorComponent | ApiV1ArtifactsArchiveCreateWebsiteUrlErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ArtifactsArchiveCreateActualAvailabilityErrorComponent
        | ApiV1ArtifactsArchiveCreateAnnotationsErrorComponent
        | ApiV1ArtifactsArchiveCreateAppVersionErrorComponent
        | ApiV1ArtifactsArchiveCreateArchivedAtErrorComponent
        | ApiV1ArtifactsArchiveCreateArchivedByErrorComponent
        | ApiV1ArtifactsArchiveCreateArchivedErrorComponent
        | ApiV1ArtifactsArchiveCreateArchivedReasonErrorComponent
        | ApiV1ArtifactsArchiveCreateChangelogErrorComponent
        | ApiV1ArtifactsArchiveCreateContentUrlErrorComponent
        | ApiV1ArtifactsArchiveCreateCreatedByComponentErrorComponent
        | ApiV1ArtifactsArchiveCreateCreatedByUserErrorComponent
        | ApiV1ArtifactsArchiveCreateCriticalityErrorComponent
        | ApiV1ArtifactsArchiveCreateDebugModeErrorComponent
        | ApiV1ArtifactsArchiveCreateDefaultConfigErrorComponent
        | ApiV1ArtifactsArchiveCreateDeprecatedErrorComponent
        | ApiV1ArtifactsArchiveCreateDescriptionErrorComponent
        | ApiV1ArtifactsArchiveCreateDigestErrorComponent
        | ApiV1ArtifactsArchiveCreateDiscoveryEnabledErrorComponent
        | ApiV1ArtifactsArchiveCreateDisplayNameErrorComponent
        | ApiV1ArtifactsArchiveCreateKindErrorComponent
        | ApiV1ArtifactsArchiveCreateLabelsErrorComponent
        | ApiV1ArtifactsArchiveCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1ArtifactsArchiveCreateLicenseErrorComponent
        | ApiV1ArtifactsArchiveCreateManagedByContentTypeErrorComponent
        | ApiV1ArtifactsArchiveCreateManagedByObjectIdErrorComponent
        | ApiV1ArtifactsArchiveCreateMetadataErrorComponent
        | ApiV1ArtifactsArchiveCreateMirroredAtErrorComponent
        | ApiV1ArtifactsArchiveCreateMirroredContentUrlErrorComponent
        | ApiV1ArtifactsArchiveCreateMirroredErrorComponent
        | ApiV1ArtifactsArchiveCreateModifiedByUserErrorComponent
        | ApiV1ArtifactsArchiveCreateNameErrorComponent
        | ApiV1ArtifactsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1ArtifactsArchiveCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1ArtifactsArchiveCreatePlatformServiceErrorComponent
        | ApiV1ArtifactsArchiveCreatePrereleaseErrorComponent
        | ApiV1ArtifactsArchiveCreateProviderErrorComponent
        | ApiV1ArtifactsArchiveCreateProviderIdErrorComponent
        | ApiV1ArtifactsArchiveCreateProviderReferenceErrorComponent
        | ApiV1ArtifactsArchiveCreateReadmeMdErrorComponent
        | ApiV1ArtifactsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1ArtifactsArchiveCreateScopeErrorComponent
        | ApiV1ArtifactsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1ArtifactsArchiveCreateSlaTargetErrorComponent
        | ApiV1ArtifactsArchiveCreateSlaWindowDaysErrorComponent
        | ApiV1ArtifactsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1ArtifactsArchiveCreateSloTargetErrorComponent
        | ApiV1ArtifactsArchiveCreateSloWindowDaysErrorComponent
        | ApiV1ArtifactsArchiveCreateSourceUrlsErrorComponent
        | ApiV1ArtifactsArchiveCreateSpecErrorComponent
        | ApiV1ArtifactsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1ArtifactsArchiveCreateVersionErrorComponent
        | ApiV1ArtifactsArchiveCreateWebsiteUrlErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_artifacts_archive_create_actual_availability_error_component import (
            ApiV1ArtifactsArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_annotations_error_component import (
            ApiV1ArtifactsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_app_version_error_component import (
            ApiV1ArtifactsArchiveCreateAppVersionErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_archived_at_error_component import (
            ApiV1ArtifactsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_archived_by_error_component import (
            ApiV1ArtifactsArchiveCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_archived_error_component import (
            ApiV1ArtifactsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_archived_reason_error_component import (
            ApiV1ArtifactsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_changelog_error_component import (
            ApiV1ArtifactsArchiveCreateChangelogErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_content_url_error_component import (
            ApiV1ArtifactsArchiveCreateContentUrlErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_created_by_component_error_component import (
            ApiV1ArtifactsArchiveCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_criticality_error_component import (
            ApiV1ArtifactsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_debug_mode_error_component import (
            ApiV1ArtifactsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_default_config_error_component import (
            ApiV1ArtifactsArchiveCreateDefaultConfigErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_deprecated_error_component import (
            ApiV1ArtifactsArchiveCreateDeprecatedErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_description_error_component import (
            ApiV1ArtifactsArchiveCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_digest_error_component import (
            ApiV1ArtifactsArchiveCreateDigestErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_discovery_enabled_error_component import (
            ApiV1ArtifactsArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_display_name_error_component import (
            ApiV1ArtifactsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_kind_error_component import (
            ApiV1ArtifactsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_labels_error_component import (
            ApiV1ArtifactsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactsArchiveCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_license_error_component import (
            ApiV1ArtifactsArchiveCreateLicenseErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_managed_by_content_type_error_component import (
            ApiV1ArtifactsArchiveCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_managed_by_object_id_error_component import (
            ApiV1ArtifactsArchiveCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_metadata_error_component import (
            ApiV1ArtifactsArchiveCreateMetadataErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_mirrored_at_error_component import (
            ApiV1ArtifactsArchiveCreateMirroredAtErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_mirrored_content_url_error_component import (
            ApiV1ArtifactsArchiveCreateMirroredContentUrlErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_mirrored_error_component import (
            ApiV1ArtifactsArchiveCreateMirroredErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_modified_by_user_error_component import (
            ApiV1ArtifactsArchiveCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_name_error_component import (
            ApiV1ArtifactsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_non_field_errors_error_component import (
            ApiV1ArtifactsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_platform_dns_record_created_error_component import (
            ApiV1ArtifactsArchiveCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_platform_service_error_component import (
            ApiV1ArtifactsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_prerelease_error_component import (
            ApiV1ArtifactsArchiveCreatePrereleaseErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_provider_error_component import (
            ApiV1ArtifactsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_provider_id_error_component import (
            ApiV1ArtifactsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_provider_reference_error_component import (
            ApiV1ArtifactsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_readme_md_error_component import (
            ApiV1ArtifactsArchiveCreateReadmeMdErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_reconciliation_enabled_error_component import (
            ApiV1ArtifactsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_scope_error_component import (
            ApiV1ArtifactsArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_sla_availability_error_component import (
            ApiV1ArtifactsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_sla_target_error_component import (
            ApiV1ArtifactsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_sla_window_days_error_component import (
            ApiV1ArtifactsArchiveCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_slo_availability_error_component import (
            ApiV1ArtifactsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_slo_target_error_component import (
            ApiV1ArtifactsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_slo_window_days_error_component import (
            ApiV1ArtifactsArchiveCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_source_urls_error_component import (
            ApiV1ArtifactsArchiveCreateSourceUrlsErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_spec_error_component import (
            ApiV1ArtifactsArchiveCreateSpecErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_target_availability_error_component import (
            ApiV1ArtifactsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_version_error_component import (
            ApiV1ArtifactsArchiveCreateVersionErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_website_url_error_component import (
            ApiV1ArtifactsArchiveCreateWebsiteUrlErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1ArtifactsArchiveCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateContentUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateWebsiteUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateSourceUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateAppVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateLicenseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateReadmeMdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateChangelogErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateDefaultConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateMirroredErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateMirroredContentUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateMirroredAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateDigestErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateDeprecatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreatePrereleaseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateMetadataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsArchiveCreateModifiedByUserErrorComponent):
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
        from ..models.api_v1_artifacts_archive_create_actual_availability_error_component import (
            ApiV1ArtifactsArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_annotations_error_component import (
            ApiV1ArtifactsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_app_version_error_component import (
            ApiV1ArtifactsArchiveCreateAppVersionErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_archived_at_error_component import (
            ApiV1ArtifactsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_archived_by_error_component import (
            ApiV1ArtifactsArchiveCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_archived_error_component import (
            ApiV1ArtifactsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_archived_reason_error_component import (
            ApiV1ArtifactsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_changelog_error_component import (
            ApiV1ArtifactsArchiveCreateChangelogErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_content_url_error_component import (
            ApiV1ArtifactsArchiveCreateContentUrlErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_created_by_component_error_component import (
            ApiV1ArtifactsArchiveCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_created_by_user_error_component import (
            ApiV1ArtifactsArchiveCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_criticality_error_component import (
            ApiV1ArtifactsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_debug_mode_error_component import (
            ApiV1ArtifactsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_default_config_error_component import (
            ApiV1ArtifactsArchiveCreateDefaultConfigErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_deprecated_error_component import (
            ApiV1ArtifactsArchiveCreateDeprecatedErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_description_error_component import (
            ApiV1ArtifactsArchiveCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_digest_error_component import (
            ApiV1ArtifactsArchiveCreateDigestErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_discovery_enabled_error_component import (
            ApiV1ArtifactsArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_display_name_error_component import (
            ApiV1ArtifactsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_kind_error_component import (
            ApiV1ArtifactsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_labels_error_component import (
            ApiV1ArtifactsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactsArchiveCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_license_error_component import (
            ApiV1ArtifactsArchiveCreateLicenseErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_managed_by_content_type_error_component import (
            ApiV1ArtifactsArchiveCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_managed_by_object_id_error_component import (
            ApiV1ArtifactsArchiveCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_metadata_error_component import (
            ApiV1ArtifactsArchiveCreateMetadataErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_mirrored_at_error_component import (
            ApiV1ArtifactsArchiveCreateMirroredAtErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_mirrored_content_url_error_component import (
            ApiV1ArtifactsArchiveCreateMirroredContentUrlErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_mirrored_error_component import (
            ApiV1ArtifactsArchiveCreateMirroredErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_modified_by_user_error_component import (
            ApiV1ArtifactsArchiveCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_name_error_component import (
            ApiV1ArtifactsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_non_field_errors_error_component import (
            ApiV1ArtifactsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_platform_dns_record_created_error_component import (
            ApiV1ArtifactsArchiveCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_platform_service_error_component import (
            ApiV1ArtifactsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_prerelease_error_component import (
            ApiV1ArtifactsArchiveCreatePrereleaseErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_provider_error_component import (
            ApiV1ArtifactsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_provider_id_error_component import (
            ApiV1ArtifactsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_provider_reference_error_component import (
            ApiV1ArtifactsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_readme_md_error_component import (
            ApiV1ArtifactsArchiveCreateReadmeMdErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_reconciliation_enabled_error_component import (
            ApiV1ArtifactsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_scope_error_component import (
            ApiV1ArtifactsArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_sla_availability_error_component import (
            ApiV1ArtifactsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_sla_target_error_component import (
            ApiV1ArtifactsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_sla_window_days_error_component import (
            ApiV1ArtifactsArchiveCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_slo_availability_error_component import (
            ApiV1ArtifactsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_slo_target_error_component import (
            ApiV1ArtifactsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_slo_window_days_error_component import (
            ApiV1ArtifactsArchiveCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_source_urls_error_component import (
            ApiV1ArtifactsArchiveCreateSourceUrlsErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_spec_error_component import (
            ApiV1ArtifactsArchiveCreateSpecErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_target_availability_error_component import (
            ApiV1ArtifactsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_version_error_component import (
            ApiV1ArtifactsArchiveCreateVersionErrorComponent,
        )
        from ..models.api_v1_artifacts_archive_create_website_url_error_component import (
            ApiV1ArtifactsArchiveCreateWebsiteUrlErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ArtifactsArchiveCreateActualAvailabilityErrorComponent
                | ApiV1ArtifactsArchiveCreateAnnotationsErrorComponent
                | ApiV1ArtifactsArchiveCreateAppVersionErrorComponent
                | ApiV1ArtifactsArchiveCreateArchivedAtErrorComponent
                | ApiV1ArtifactsArchiveCreateArchivedByErrorComponent
                | ApiV1ArtifactsArchiveCreateArchivedErrorComponent
                | ApiV1ArtifactsArchiveCreateArchivedReasonErrorComponent
                | ApiV1ArtifactsArchiveCreateChangelogErrorComponent
                | ApiV1ArtifactsArchiveCreateContentUrlErrorComponent
                | ApiV1ArtifactsArchiveCreateCreatedByComponentErrorComponent
                | ApiV1ArtifactsArchiveCreateCreatedByUserErrorComponent
                | ApiV1ArtifactsArchiveCreateCriticalityErrorComponent
                | ApiV1ArtifactsArchiveCreateDebugModeErrorComponent
                | ApiV1ArtifactsArchiveCreateDefaultConfigErrorComponent
                | ApiV1ArtifactsArchiveCreateDeprecatedErrorComponent
                | ApiV1ArtifactsArchiveCreateDescriptionErrorComponent
                | ApiV1ArtifactsArchiveCreateDigestErrorComponent
                | ApiV1ArtifactsArchiveCreateDiscoveryEnabledErrorComponent
                | ApiV1ArtifactsArchiveCreateDisplayNameErrorComponent
                | ApiV1ArtifactsArchiveCreateKindErrorComponent
                | ApiV1ArtifactsArchiveCreateLabelsErrorComponent
                | ApiV1ArtifactsArchiveCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1ArtifactsArchiveCreateLicenseErrorComponent
                | ApiV1ArtifactsArchiveCreateManagedByContentTypeErrorComponent
                | ApiV1ArtifactsArchiveCreateManagedByObjectIdErrorComponent
                | ApiV1ArtifactsArchiveCreateMetadataErrorComponent
                | ApiV1ArtifactsArchiveCreateMirroredAtErrorComponent
                | ApiV1ArtifactsArchiveCreateMirroredContentUrlErrorComponent
                | ApiV1ArtifactsArchiveCreateMirroredErrorComponent
                | ApiV1ArtifactsArchiveCreateModifiedByUserErrorComponent
                | ApiV1ArtifactsArchiveCreateNameErrorComponent
                | ApiV1ArtifactsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1ArtifactsArchiveCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1ArtifactsArchiveCreatePlatformServiceErrorComponent
                | ApiV1ArtifactsArchiveCreatePrereleaseErrorComponent
                | ApiV1ArtifactsArchiveCreateProviderErrorComponent
                | ApiV1ArtifactsArchiveCreateProviderIdErrorComponent
                | ApiV1ArtifactsArchiveCreateProviderReferenceErrorComponent
                | ApiV1ArtifactsArchiveCreateReadmeMdErrorComponent
                | ApiV1ArtifactsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1ArtifactsArchiveCreateScopeErrorComponent
                | ApiV1ArtifactsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1ArtifactsArchiveCreateSlaTargetErrorComponent
                | ApiV1ArtifactsArchiveCreateSlaWindowDaysErrorComponent
                | ApiV1ArtifactsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1ArtifactsArchiveCreateSloTargetErrorComponent
                | ApiV1ArtifactsArchiveCreateSloWindowDaysErrorComponent
                | ApiV1ArtifactsArchiveCreateSourceUrlsErrorComponent
                | ApiV1ArtifactsArchiveCreateSpecErrorComponent
                | ApiV1ArtifactsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1ArtifactsArchiveCreateVersionErrorComponent
                | ApiV1ArtifactsArchiveCreateWebsiteUrlErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_0 = (
                        ApiV1ArtifactsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_1 = (
                        ApiV1ArtifactsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_2 = (
                        ApiV1ArtifactsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_3 = (
                        ApiV1ArtifactsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_4 = (
                        ApiV1ArtifactsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_5 = (
                        ApiV1ArtifactsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_6 = (
                        ApiV1ArtifactsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_7 = (
                        ApiV1ArtifactsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_8 = (
                        ApiV1ArtifactsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_9 = (
                        ApiV1ArtifactsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_10 = (
                        ApiV1ArtifactsArchiveCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_11 = (
                        ApiV1ArtifactsArchiveCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_12 = (
                        ApiV1ArtifactsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_13 = (
                        ApiV1ArtifactsArchiveCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_14 = (
                        ApiV1ArtifactsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_15 = (
                        ApiV1ArtifactsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_16 = (
                        ApiV1ArtifactsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_17 = (
                        ApiV1ArtifactsArchiveCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_18 = (
                        ApiV1ArtifactsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_19 = (
                        ApiV1ArtifactsArchiveCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_20 = (
                        ApiV1ArtifactsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_21 = (
                        ApiV1ArtifactsArchiveCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_22 = (
                        ApiV1ArtifactsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_23 = (
                        ApiV1ArtifactsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_24 = (
                        ApiV1ArtifactsArchiveCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_25 = (
                        ApiV1ArtifactsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_26 = (
                        ApiV1ArtifactsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_27 = (
                        ApiV1ArtifactsArchiveCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_28 = (
                        ApiV1ArtifactsArchiveCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_29 = (
                        ApiV1ArtifactsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_30 = (
                        ApiV1ArtifactsArchiveCreateContentUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_31 = (
                        ApiV1ArtifactsArchiveCreateWebsiteUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_32 = (
                        ApiV1ArtifactsArchiveCreateSourceUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_33 = (
                        ApiV1ArtifactsArchiveCreateVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_34 = (
                        ApiV1ArtifactsArchiveCreateAppVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_35 = (
                        ApiV1ArtifactsArchiveCreateLicenseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_36 = (
                        ApiV1ArtifactsArchiveCreateReadmeMdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_37 = (
                        ApiV1ArtifactsArchiveCreateChangelogErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_38 = (
                        ApiV1ArtifactsArchiveCreateSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_39 = (
                        ApiV1ArtifactsArchiveCreateDefaultConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_40 = (
                        ApiV1ArtifactsArchiveCreateMirroredErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_41 = (
                        ApiV1ArtifactsArchiveCreateMirroredContentUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_42 = (
                        ApiV1ArtifactsArchiveCreateMirroredAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_43 = (
                        ApiV1ArtifactsArchiveCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_44 = (
                        ApiV1ArtifactsArchiveCreateDigestErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_45 = (
                        ApiV1ArtifactsArchiveCreateDeprecatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_46 = (
                        ApiV1ArtifactsArchiveCreatePrereleaseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_47 = (
                        ApiV1ArtifactsArchiveCreateMetadataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_48 = (
                        ApiV1ArtifactsArchiveCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_49 = (
                        ApiV1ArtifactsArchiveCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_archive_create_error_type_50 = (
                        ApiV1ArtifactsArchiveCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_archive_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_artifacts_archive_create_error_type_51 = (
                    ApiV1ArtifactsArchiveCreateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_artifacts_archive_create_error_type_51

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_artifacts_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_artifacts_archive_create_validation_error.additional_properties = d
        return api_v1_artifacts_archive_create_validation_error

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
