from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_artifacts_partial_update_actual_availability_error_component import (
        ApiV1ArtifactsPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_annotations_error_component import (
        ApiV1ArtifactsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_app_version_error_component import (
        ApiV1ArtifactsPartialUpdateAppVersionErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_archived_at_error_component import (
        ApiV1ArtifactsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_archived_by_error_component import (
        ApiV1ArtifactsPartialUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_archived_error_component import (
        ApiV1ArtifactsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_archived_reason_error_component import (
        ApiV1ArtifactsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_changelog_error_component import (
        ApiV1ArtifactsPartialUpdateChangelogErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_content_url_error_component import (
        ApiV1ArtifactsPartialUpdateContentUrlErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_created_by_component_error_component import (
        ApiV1ArtifactsPartialUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_created_by_user_error_component import (
        ApiV1ArtifactsPartialUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_criticality_error_component import (
        ApiV1ArtifactsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_debug_mode_error_component import (
        ApiV1ArtifactsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_default_config_error_component import (
        ApiV1ArtifactsPartialUpdateDefaultConfigErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_deprecated_error_component import (
        ApiV1ArtifactsPartialUpdateDeprecatedErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_description_error_component import (
        ApiV1ArtifactsPartialUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_digest_error_component import (
        ApiV1ArtifactsPartialUpdateDigestErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_discovery_enabled_error_component import (
        ApiV1ArtifactsPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_display_name_error_component import (
        ApiV1ArtifactsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_kind_error_component import (
        ApiV1ArtifactsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_labels_error_component import (
        ApiV1ArtifactsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1ArtifactsPartialUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_license_error_component import (
        ApiV1ArtifactsPartialUpdateLicenseErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_managed_by_content_type_error_component import (
        ApiV1ArtifactsPartialUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_managed_by_object_id_error_component import (
        ApiV1ArtifactsPartialUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_metadata_error_component import (
        ApiV1ArtifactsPartialUpdateMetadataErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_mirrored_at_error_component import (
        ApiV1ArtifactsPartialUpdateMirroredAtErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_mirrored_content_url_error_component import (
        ApiV1ArtifactsPartialUpdateMirroredContentUrlErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_mirrored_error_component import (
        ApiV1ArtifactsPartialUpdateMirroredErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_modified_by_user_error_component import (
        ApiV1ArtifactsPartialUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_name_error_component import (
        ApiV1ArtifactsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_non_field_errors_error_component import (
        ApiV1ArtifactsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_platform_dns_record_created_error_component import (
        ApiV1ArtifactsPartialUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_platform_service_error_component import (
        ApiV1ArtifactsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_prerelease_error_component import (
        ApiV1ArtifactsPartialUpdatePrereleaseErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_provider_error_component import (
        ApiV1ArtifactsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_provider_id_error_component import (
        ApiV1ArtifactsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_provider_reference_error_component import (
        ApiV1ArtifactsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_readme_md_error_component import (
        ApiV1ArtifactsPartialUpdateReadmeMdErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_reconciliation_enabled_error_component import (
        ApiV1ArtifactsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_scope_error_component import (
        ApiV1ArtifactsPartialUpdateScopeErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_sla_availability_error_component import (
        ApiV1ArtifactsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_sla_target_error_component import (
        ApiV1ArtifactsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_sla_window_days_error_component import (
        ApiV1ArtifactsPartialUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_slo_availability_error_component import (
        ApiV1ArtifactsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_slo_target_error_component import (
        ApiV1ArtifactsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_slo_window_days_error_component import (
        ApiV1ArtifactsPartialUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_source_urls_error_component import (
        ApiV1ArtifactsPartialUpdateSourceUrlsErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_spec_error_component import (
        ApiV1ArtifactsPartialUpdateSpecErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_target_availability_error_component import (
        ApiV1ArtifactsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_version_error_component import (
        ApiV1ArtifactsPartialUpdateVersionErrorComponent,
    )
    from ..models.api_v1_artifacts_partial_update_website_url_error_component import (
        ApiV1ArtifactsPartialUpdateWebsiteUrlErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ArtifactsPartialUpdateValidationError")


@_attrs_define
class ApiV1ArtifactsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ArtifactsPartialUpdateActualAvailabilityErrorComponent |
            ApiV1ArtifactsPartialUpdateAnnotationsErrorComponent | ApiV1ArtifactsPartialUpdateAppVersionErrorComponent |
            ApiV1ArtifactsPartialUpdateArchivedAtErrorComponent | ApiV1ArtifactsPartialUpdateArchivedByErrorComponent |
            ApiV1ArtifactsPartialUpdateArchivedErrorComponent | ApiV1ArtifactsPartialUpdateArchivedReasonErrorComponent |
            ApiV1ArtifactsPartialUpdateChangelogErrorComponent | ApiV1ArtifactsPartialUpdateContentUrlErrorComponent |
            ApiV1ArtifactsPartialUpdateCreatedByComponentErrorComponent |
            ApiV1ArtifactsPartialUpdateCreatedByUserErrorComponent | ApiV1ArtifactsPartialUpdateCriticalityErrorComponent |
            ApiV1ArtifactsPartialUpdateDebugModeErrorComponent | ApiV1ArtifactsPartialUpdateDefaultConfigErrorComponent |
            ApiV1ArtifactsPartialUpdateDeprecatedErrorComponent | ApiV1ArtifactsPartialUpdateDescriptionErrorComponent |
            ApiV1ArtifactsPartialUpdateDigestErrorComponent | ApiV1ArtifactsPartialUpdateDiscoveryEnabledErrorComponent |
            ApiV1ArtifactsPartialUpdateDisplayNameErrorComponent | ApiV1ArtifactsPartialUpdateKindErrorComponent |
            ApiV1ArtifactsPartialUpdateLabelsErrorComponent |
            ApiV1ArtifactsPartialUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1ArtifactsPartialUpdateLicenseErrorComponent | ApiV1ArtifactsPartialUpdateManagedByContentTypeErrorComponent
            | ApiV1ArtifactsPartialUpdateManagedByObjectIdErrorComponent | ApiV1ArtifactsPartialUpdateMetadataErrorComponent
            | ApiV1ArtifactsPartialUpdateMirroredAtErrorComponent |
            ApiV1ArtifactsPartialUpdateMirroredContentUrlErrorComponent | ApiV1ArtifactsPartialUpdateMirroredErrorComponent
            | ApiV1ArtifactsPartialUpdateModifiedByUserErrorComponent | ApiV1ArtifactsPartialUpdateNameErrorComponent |
            ApiV1ArtifactsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1ArtifactsPartialUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1ArtifactsPartialUpdatePlatformServiceErrorComponent | ApiV1ArtifactsPartialUpdatePrereleaseErrorComponent |
            ApiV1ArtifactsPartialUpdateProviderErrorComponent | ApiV1ArtifactsPartialUpdateProviderIdErrorComponent |
            ApiV1ArtifactsPartialUpdateProviderReferenceErrorComponent | ApiV1ArtifactsPartialUpdateReadmeMdErrorComponent |
            ApiV1ArtifactsPartialUpdateReconciliationEnabledErrorComponent | ApiV1ArtifactsPartialUpdateScopeErrorComponent
            | ApiV1ArtifactsPartialUpdateSlaAvailabilityErrorComponent | ApiV1ArtifactsPartialUpdateSlaTargetErrorComponent
            | ApiV1ArtifactsPartialUpdateSlaWindowDaysErrorComponent |
            ApiV1ArtifactsPartialUpdateSloAvailabilityErrorComponent | ApiV1ArtifactsPartialUpdateSloTargetErrorComponent |
            ApiV1ArtifactsPartialUpdateSloWindowDaysErrorComponent | ApiV1ArtifactsPartialUpdateSourceUrlsErrorComponent |
            ApiV1ArtifactsPartialUpdateSpecErrorComponent | ApiV1ArtifactsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1ArtifactsPartialUpdateVersionErrorComponent | ApiV1ArtifactsPartialUpdateWebsiteUrlErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ArtifactsPartialUpdateActualAvailabilityErrorComponent
        | ApiV1ArtifactsPartialUpdateAnnotationsErrorComponent
        | ApiV1ArtifactsPartialUpdateAppVersionErrorComponent
        | ApiV1ArtifactsPartialUpdateArchivedAtErrorComponent
        | ApiV1ArtifactsPartialUpdateArchivedByErrorComponent
        | ApiV1ArtifactsPartialUpdateArchivedErrorComponent
        | ApiV1ArtifactsPartialUpdateArchivedReasonErrorComponent
        | ApiV1ArtifactsPartialUpdateChangelogErrorComponent
        | ApiV1ArtifactsPartialUpdateContentUrlErrorComponent
        | ApiV1ArtifactsPartialUpdateCreatedByComponentErrorComponent
        | ApiV1ArtifactsPartialUpdateCreatedByUserErrorComponent
        | ApiV1ArtifactsPartialUpdateCriticalityErrorComponent
        | ApiV1ArtifactsPartialUpdateDebugModeErrorComponent
        | ApiV1ArtifactsPartialUpdateDefaultConfigErrorComponent
        | ApiV1ArtifactsPartialUpdateDeprecatedErrorComponent
        | ApiV1ArtifactsPartialUpdateDescriptionErrorComponent
        | ApiV1ArtifactsPartialUpdateDigestErrorComponent
        | ApiV1ArtifactsPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1ArtifactsPartialUpdateDisplayNameErrorComponent
        | ApiV1ArtifactsPartialUpdateKindErrorComponent
        | ApiV1ArtifactsPartialUpdateLabelsErrorComponent
        | ApiV1ArtifactsPartialUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1ArtifactsPartialUpdateLicenseErrorComponent
        | ApiV1ArtifactsPartialUpdateManagedByContentTypeErrorComponent
        | ApiV1ArtifactsPartialUpdateManagedByObjectIdErrorComponent
        | ApiV1ArtifactsPartialUpdateMetadataErrorComponent
        | ApiV1ArtifactsPartialUpdateMirroredAtErrorComponent
        | ApiV1ArtifactsPartialUpdateMirroredContentUrlErrorComponent
        | ApiV1ArtifactsPartialUpdateMirroredErrorComponent
        | ApiV1ArtifactsPartialUpdateModifiedByUserErrorComponent
        | ApiV1ArtifactsPartialUpdateNameErrorComponent
        | ApiV1ArtifactsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1ArtifactsPartialUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1ArtifactsPartialUpdatePlatformServiceErrorComponent
        | ApiV1ArtifactsPartialUpdatePrereleaseErrorComponent
        | ApiV1ArtifactsPartialUpdateProviderErrorComponent
        | ApiV1ArtifactsPartialUpdateProviderIdErrorComponent
        | ApiV1ArtifactsPartialUpdateProviderReferenceErrorComponent
        | ApiV1ArtifactsPartialUpdateReadmeMdErrorComponent
        | ApiV1ArtifactsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1ArtifactsPartialUpdateScopeErrorComponent
        | ApiV1ArtifactsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1ArtifactsPartialUpdateSlaTargetErrorComponent
        | ApiV1ArtifactsPartialUpdateSlaWindowDaysErrorComponent
        | ApiV1ArtifactsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1ArtifactsPartialUpdateSloTargetErrorComponent
        | ApiV1ArtifactsPartialUpdateSloWindowDaysErrorComponent
        | ApiV1ArtifactsPartialUpdateSourceUrlsErrorComponent
        | ApiV1ArtifactsPartialUpdateSpecErrorComponent
        | ApiV1ArtifactsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1ArtifactsPartialUpdateVersionErrorComponent
        | ApiV1ArtifactsPartialUpdateWebsiteUrlErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_artifacts_partial_update_actual_availability_error_component import (
            ApiV1ArtifactsPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_annotations_error_component import (
            ApiV1ArtifactsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_app_version_error_component import (
            ApiV1ArtifactsPartialUpdateAppVersionErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_archived_at_error_component import (
            ApiV1ArtifactsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_archived_by_error_component import (
            ApiV1ArtifactsPartialUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_archived_error_component import (
            ApiV1ArtifactsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_archived_reason_error_component import (
            ApiV1ArtifactsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_changelog_error_component import (
            ApiV1ArtifactsPartialUpdateChangelogErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_content_url_error_component import (
            ApiV1ArtifactsPartialUpdateContentUrlErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_created_by_component_error_component import (
            ApiV1ArtifactsPartialUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_criticality_error_component import (
            ApiV1ArtifactsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_debug_mode_error_component import (
            ApiV1ArtifactsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_default_config_error_component import (
            ApiV1ArtifactsPartialUpdateDefaultConfigErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_deprecated_error_component import (
            ApiV1ArtifactsPartialUpdateDeprecatedErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_description_error_component import (
            ApiV1ArtifactsPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_digest_error_component import (
            ApiV1ArtifactsPartialUpdateDigestErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_discovery_enabled_error_component import (
            ApiV1ArtifactsPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_display_name_error_component import (
            ApiV1ArtifactsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_kind_error_component import (
            ApiV1ArtifactsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_labels_error_component import (
            ApiV1ArtifactsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactsPartialUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_license_error_component import (
            ApiV1ArtifactsPartialUpdateLicenseErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_managed_by_content_type_error_component import (
            ApiV1ArtifactsPartialUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_managed_by_object_id_error_component import (
            ApiV1ArtifactsPartialUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_metadata_error_component import (
            ApiV1ArtifactsPartialUpdateMetadataErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_mirrored_at_error_component import (
            ApiV1ArtifactsPartialUpdateMirroredAtErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_mirrored_content_url_error_component import (
            ApiV1ArtifactsPartialUpdateMirroredContentUrlErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_mirrored_error_component import (
            ApiV1ArtifactsPartialUpdateMirroredErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_modified_by_user_error_component import (
            ApiV1ArtifactsPartialUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_name_error_component import (
            ApiV1ArtifactsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_non_field_errors_error_component import (
            ApiV1ArtifactsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_platform_dns_record_created_error_component import (
            ApiV1ArtifactsPartialUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_platform_service_error_component import (
            ApiV1ArtifactsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_prerelease_error_component import (
            ApiV1ArtifactsPartialUpdatePrereleaseErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_provider_error_component import (
            ApiV1ArtifactsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_provider_id_error_component import (
            ApiV1ArtifactsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_provider_reference_error_component import (
            ApiV1ArtifactsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_readme_md_error_component import (
            ApiV1ArtifactsPartialUpdateReadmeMdErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_reconciliation_enabled_error_component import (
            ApiV1ArtifactsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_scope_error_component import (
            ApiV1ArtifactsPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_sla_availability_error_component import (
            ApiV1ArtifactsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_sla_target_error_component import (
            ApiV1ArtifactsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_sla_window_days_error_component import (
            ApiV1ArtifactsPartialUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_slo_availability_error_component import (
            ApiV1ArtifactsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_slo_target_error_component import (
            ApiV1ArtifactsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_slo_window_days_error_component import (
            ApiV1ArtifactsPartialUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_source_urls_error_component import (
            ApiV1ArtifactsPartialUpdateSourceUrlsErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_spec_error_component import (
            ApiV1ArtifactsPartialUpdateSpecErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_target_availability_error_component import (
            ApiV1ArtifactsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_version_error_component import (
            ApiV1ArtifactsPartialUpdateVersionErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_website_url_error_component import (
            ApiV1ArtifactsPartialUpdateWebsiteUrlErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1ArtifactsPartialUpdateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateContentUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateWebsiteUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateSourceUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateAppVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateLicenseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateReadmeMdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateChangelogErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateDefaultConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateMirroredErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateMirroredContentUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateMirroredAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateDigestErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateDeprecatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdatePrereleaseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateMetadataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsPartialUpdateModifiedByUserErrorComponent):
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
        from ..models.api_v1_artifacts_partial_update_actual_availability_error_component import (
            ApiV1ArtifactsPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_annotations_error_component import (
            ApiV1ArtifactsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_app_version_error_component import (
            ApiV1ArtifactsPartialUpdateAppVersionErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_archived_at_error_component import (
            ApiV1ArtifactsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_archived_by_error_component import (
            ApiV1ArtifactsPartialUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_archived_error_component import (
            ApiV1ArtifactsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_archived_reason_error_component import (
            ApiV1ArtifactsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_changelog_error_component import (
            ApiV1ArtifactsPartialUpdateChangelogErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_content_url_error_component import (
            ApiV1ArtifactsPartialUpdateContentUrlErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_created_by_component_error_component import (
            ApiV1ArtifactsPartialUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_created_by_user_error_component import (
            ApiV1ArtifactsPartialUpdateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_criticality_error_component import (
            ApiV1ArtifactsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_debug_mode_error_component import (
            ApiV1ArtifactsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_default_config_error_component import (
            ApiV1ArtifactsPartialUpdateDefaultConfigErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_deprecated_error_component import (
            ApiV1ArtifactsPartialUpdateDeprecatedErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_description_error_component import (
            ApiV1ArtifactsPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_digest_error_component import (
            ApiV1ArtifactsPartialUpdateDigestErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_discovery_enabled_error_component import (
            ApiV1ArtifactsPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_display_name_error_component import (
            ApiV1ArtifactsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_kind_error_component import (
            ApiV1ArtifactsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_labels_error_component import (
            ApiV1ArtifactsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactsPartialUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_license_error_component import (
            ApiV1ArtifactsPartialUpdateLicenseErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_managed_by_content_type_error_component import (
            ApiV1ArtifactsPartialUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_managed_by_object_id_error_component import (
            ApiV1ArtifactsPartialUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_metadata_error_component import (
            ApiV1ArtifactsPartialUpdateMetadataErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_mirrored_at_error_component import (
            ApiV1ArtifactsPartialUpdateMirroredAtErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_mirrored_content_url_error_component import (
            ApiV1ArtifactsPartialUpdateMirroredContentUrlErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_mirrored_error_component import (
            ApiV1ArtifactsPartialUpdateMirroredErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_modified_by_user_error_component import (
            ApiV1ArtifactsPartialUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_name_error_component import (
            ApiV1ArtifactsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_non_field_errors_error_component import (
            ApiV1ArtifactsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_platform_dns_record_created_error_component import (
            ApiV1ArtifactsPartialUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_platform_service_error_component import (
            ApiV1ArtifactsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_prerelease_error_component import (
            ApiV1ArtifactsPartialUpdatePrereleaseErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_provider_error_component import (
            ApiV1ArtifactsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_provider_id_error_component import (
            ApiV1ArtifactsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_provider_reference_error_component import (
            ApiV1ArtifactsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_readme_md_error_component import (
            ApiV1ArtifactsPartialUpdateReadmeMdErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_reconciliation_enabled_error_component import (
            ApiV1ArtifactsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_scope_error_component import (
            ApiV1ArtifactsPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_sla_availability_error_component import (
            ApiV1ArtifactsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_sla_target_error_component import (
            ApiV1ArtifactsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_sla_window_days_error_component import (
            ApiV1ArtifactsPartialUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_slo_availability_error_component import (
            ApiV1ArtifactsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_slo_target_error_component import (
            ApiV1ArtifactsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_slo_window_days_error_component import (
            ApiV1ArtifactsPartialUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_source_urls_error_component import (
            ApiV1ArtifactsPartialUpdateSourceUrlsErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_spec_error_component import (
            ApiV1ArtifactsPartialUpdateSpecErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_target_availability_error_component import (
            ApiV1ArtifactsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_version_error_component import (
            ApiV1ArtifactsPartialUpdateVersionErrorComponent,
        )
        from ..models.api_v1_artifacts_partial_update_website_url_error_component import (
            ApiV1ArtifactsPartialUpdateWebsiteUrlErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ArtifactsPartialUpdateActualAvailabilityErrorComponent
                | ApiV1ArtifactsPartialUpdateAnnotationsErrorComponent
                | ApiV1ArtifactsPartialUpdateAppVersionErrorComponent
                | ApiV1ArtifactsPartialUpdateArchivedAtErrorComponent
                | ApiV1ArtifactsPartialUpdateArchivedByErrorComponent
                | ApiV1ArtifactsPartialUpdateArchivedErrorComponent
                | ApiV1ArtifactsPartialUpdateArchivedReasonErrorComponent
                | ApiV1ArtifactsPartialUpdateChangelogErrorComponent
                | ApiV1ArtifactsPartialUpdateContentUrlErrorComponent
                | ApiV1ArtifactsPartialUpdateCreatedByComponentErrorComponent
                | ApiV1ArtifactsPartialUpdateCreatedByUserErrorComponent
                | ApiV1ArtifactsPartialUpdateCriticalityErrorComponent
                | ApiV1ArtifactsPartialUpdateDebugModeErrorComponent
                | ApiV1ArtifactsPartialUpdateDefaultConfigErrorComponent
                | ApiV1ArtifactsPartialUpdateDeprecatedErrorComponent
                | ApiV1ArtifactsPartialUpdateDescriptionErrorComponent
                | ApiV1ArtifactsPartialUpdateDigestErrorComponent
                | ApiV1ArtifactsPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1ArtifactsPartialUpdateDisplayNameErrorComponent
                | ApiV1ArtifactsPartialUpdateKindErrorComponent
                | ApiV1ArtifactsPartialUpdateLabelsErrorComponent
                | ApiV1ArtifactsPartialUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1ArtifactsPartialUpdateLicenseErrorComponent
                | ApiV1ArtifactsPartialUpdateManagedByContentTypeErrorComponent
                | ApiV1ArtifactsPartialUpdateManagedByObjectIdErrorComponent
                | ApiV1ArtifactsPartialUpdateMetadataErrorComponent
                | ApiV1ArtifactsPartialUpdateMirroredAtErrorComponent
                | ApiV1ArtifactsPartialUpdateMirroredContentUrlErrorComponent
                | ApiV1ArtifactsPartialUpdateMirroredErrorComponent
                | ApiV1ArtifactsPartialUpdateModifiedByUserErrorComponent
                | ApiV1ArtifactsPartialUpdateNameErrorComponent
                | ApiV1ArtifactsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1ArtifactsPartialUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1ArtifactsPartialUpdatePlatformServiceErrorComponent
                | ApiV1ArtifactsPartialUpdatePrereleaseErrorComponent
                | ApiV1ArtifactsPartialUpdateProviderErrorComponent
                | ApiV1ArtifactsPartialUpdateProviderIdErrorComponent
                | ApiV1ArtifactsPartialUpdateProviderReferenceErrorComponent
                | ApiV1ArtifactsPartialUpdateReadmeMdErrorComponent
                | ApiV1ArtifactsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1ArtifactsPartialUpdateScopeErrorComponent
                | ApiV1ArtifactsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1ArtifactsPartialUpdateSlaTargetErrorComponent
                | ApiV1ArtifactsPartialUpdateSlaWindowDaysErrorComponent
                | ApiV1ArtifactsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1ArtifactsPartialUpdateSloTargetErrorComponent
                | ApiV1ArtifactsPartialUpdateSloWindowDaysErrorComponent
                | ApiV1ArtifactsPartialUpdateSourceUrlsErrorComponent
                | ApiV1ArtifactsPartialUpdateSpecErrorComponent
                | ApiV1ArtifactsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1ArtifactsPartialUpdateVersionErrorComponent
                | ApiV1ArtifactsPartialUpdateWebsiteUrlErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_0 = (
                        ApiV1ArtifactsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_1 = (
                        ApiV1ArtifactsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_2 = (
                        ApiV1ArtifactsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_3 = (
                        ApiV1ArtifactsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_4 = (
                        ApiV1ArtifactsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_5 = (
                        ApiV1ArtifactsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_6 = (
                        ApiV1ArtifactsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_7 = (
                        ApiV1ArtifactsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_8 = (
                        ApiV1ArtifactsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_9 = (
                        ApiV1ArtifactsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_10 = (
                        ApiV1ArtifactsPartialUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_11 = (
                        ApiV1ArtifactsPartialUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_12 = (
                        ApiV1ArtifactsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_13 = (
                        ApiV1ArtifactsPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_14 = (
                        ApiV1ArtifactsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_15 = (
                        ApiV1ArtifactsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_16 = (
                        ApiV1ArtifactsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_17 = (
                        ApiV1ArtifactsPartialUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_18 = (
                        ApiV1ArtifactsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_19 = (
                        ApiV1ArtifactsPartialUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_20 = (
                        ApiV1ArtifactsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_21 = (
                        ApiV1ArtifactsPartialUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_22 = (
                        ApiV1ArtifactsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_23 = (
                        ApiV1ArtifactsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_24 = (
                        ApiV1ArtifactsPartialUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_25 = (
                        ApiV1ArtifactsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_26 = (
                        ApiV1ArtifactsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_27 = (
                        ApiV1ArtifactsPartialUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_28 = (
                        ApiV1ArtifactsPartialUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_29 = (
                        ApiV1ArtifactsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_30 = (
                        ApiV1ArtifactsPartialUpdateContentUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_31 = (
                        ApiV1ArtifactsPartialUpdateWebsiteUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_32 = (
                        ApiV1ArtifactsPartialUpdateSourceUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_33 = (
                        ApiV1ArtifactsPartialUpdateVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_34 = (
                        ApiV1ArtifactsPartialUpdateAppVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_35 = (
                        ApiV1ArtifactsPartialUpdateLicenseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_36 = (
                        ApiV1ArtifactsPartialUpdateReadmeMdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_37 = (
                        ApiV1ArtifactsPartialUpdateChangelogErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_38 = (
                        ApiV1ArtifactsPartialUpdateSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_39 = (
                        ApiV1ArtifactsPartialUpdateDefaultConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_40 = (
                        ApiV1ArtifactsPartialUpdateMirroredErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_41 = (
                        ApiV1ArtifactsPartialUpdateMirroredContentUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_42 = (
                        ApiV1ArtifactsPartialUpdateMirroredAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_43 = (
                        ApiV1ArtifactsPartialUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_44 = (
                        ApiV1ArtifactsPartialUpdateDigestErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_45 = (
                        ApiV1ArtifactsPartialUpdateDeprecatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_46 = (
                        ApiV1ArtifactsPartialUpdatePrereleaseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_47 = (
                        ApiV1ArtifactsPartialUpdateMetadataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_48 = (
                        ApiV1ArtifactsPartialUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_49 = (
                        ApiV1ArtifactsPartialUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_partial_update_error_type_50 = (
                        ApiV1ArtifactsPartialUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_partial_update_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_artifacts_partial_update_error_type_51 = (
                    ApiV1ArtifactsPartialUpdateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_artifacts_partial_update_error_type_51

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_artifacts_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_artifacts_partial_update_validation_error.additional_properties = d
        return api_v1_artifacts_partial_update_validation_error

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
