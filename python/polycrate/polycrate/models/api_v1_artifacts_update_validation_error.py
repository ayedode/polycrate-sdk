from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_artifacts_update_actual_availability_error_component import (
        ApiV1ArtifactsUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifacts_update_annotations_error_component import (
        ApiV1ArtifactsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_artifacts_update_app_version_error_component import (
        ApiV1ArtifactsUpdateAppVersionErrorComponent,
    )
    from ..models.api_v1_artifacts_update_archived_at_error_component import (
        ApiV1ArtifactsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_artifacts_update_archived_by_error_component import (
        ApiV1ArtifactsUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_artifacts_update_archived_error_component import ApiV1ArtifactsUpdateArchivedErrorComponent
    from ..models.api_v1_artifacts_update_archived_reason_error_component import (
        ApiV1ArtifactsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_artifacts_update_changelog_error_component import ApiV1ArtifactsUpdateChangelogErrorComponent
    from ..models.api_v1_artifacts_update_content_url_error_component import (
        ApiV1ArtifactsUpdateContentUrlErrorComponent,
    )
    from ..models.api_v1_artifacts_update_created_by_component_error_component import (
        ApiV1ArtifactsUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_artifacts_update_created_by_user_error_component import (
        ApiV1ArtifactsUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_artifacts_update_criticality_error_component import (
        ApiV1ArtifactsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_artifacts_update_debug_mode_error_component import ApiV1ArtifactsUpdateDebugModeErrorComponent
    from ..models.api_v1_artifacts_update_default_config_error_component import (
        ApiV1ArtifactsUpdateDefaultConfigErrorComponent,
    )
    from ..models.api_v1_artifacts_update_deprecated_error_component import ApiV1ArtifactsUpdateDeprecatedErrorComponent
    from ..models.api_v1_artifacts_update_description_error_component import (
        ApiV1ArtifactsUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_artifacts_update_digest_error_component import ApiV1ArtifactsUpdateDigestErrorComponent
    from ..models.api_v1_artifacts_update_discovery_enabled_error_component import (
        ApiV1ArtifactsUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_artifacts_update_display_name_error_component import (
        ApiV1ArtifactsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_artifacts_update_kind_error_component import ApiV1ArtifactsUpdateKindErrorComponent
    from ..models.api_v1_artifacts_update_labels_error_component import ApiV1ArtifactsUpdateLabelsErrorComponent
    from ..models.api_v1_artifacts_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1ArtifactsUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_artifacts_update_license_error_component import ApiV1ArtifactsUpdateLicenseErrorComponent
    from ..models.api_v1_artifacts_update_managed_by_content_type_error_component import (
        ApiV1ArtifactsUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_artifacts_update_managed_by_object_id_error_component import (
        ApiV1ArtifactsUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_artifacts_update_metadata_error_component import ApiV1ArtifactsUpdateMetadataErrorComponent
    from ..models.api_v1_artifacts_update_mirrored_at_error_component import (
        ApiV1ArtifactsUpdateMirroredAtErrorComponent,
    )
    from ..models.api_v1_artifacts_update_mirrored_content_url_error_component import (
        ApiV1ArtifactsUpdateMirroredContentUrlErrorComponent,
    )
    from ..models.api_v1_artifacts_update_mirrored_error_component import ApiV1ArtifactsUpdateMirroredErrorComponent
    from ..models.api_v1_artifacts_update_modified_by_user_error_component import (
        ApiV1ArtifactsUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_artifacts_update_name_error_component import ApiV1ArtifactsUpdateNameErrorComponent
    from ..models.api_v1_artifacts_update_non_field_errors_error_component import (
        ApiV1ArtifactsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_artifacts_update_platform_dns_record_created_error_component import (
        ApiV1ArtifactsUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_artifacts_update_platform_service_error_component import (
        ApiV1ArtifactsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_artifacts_update_prerelease_error_component import ApiV1ArtifactsUpdatePrereleaseErrorComponent
    from ..models.api_v1_artifacts_update_provider_error_component import ApiV1ArtifactsUpdateProviderErrorComponent
    from ..models.api_v1_artifacts_update_provider_id_error_component import (
        ApiV1ArtifactsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_artifacts_update_provider_reference_error_component import (
        ApiV1ArtifactsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_artifacts_update_readme_md_error_component import ApiV1ArtifactsUpdateReadmeMdErrorComponent
    from ..models.api_v1_artifacts_update_reconciliation_enabled_error_component import (
        ApiV1ArtifactsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_artifacts_update_scope_error_component import ApiV1ArtifactsUpdateScopeErrorComponent
    from ..models.api_v1_artifacts_update_sla_availability_error_component import (
        ApiV1ArtifactsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifacts_update_sla_target_error_component import ApiV1ArtifactsUpdateSlaTargetErrorComponent
    from ..models.api_v1_artifacts_update_sla_window_days_error_component import (
        ApiV1ArtifactsUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifacts_update_slo_availability_error_component import (
        ApiV1ArtifactsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifacts_update_slo_target_error_component import ApiV1ArtifactsUpdateSloTargetErrorComponent
    from ..models.api_v1_artifacts_update_slo_window_days_error_component import (
        ApiV1ArtifactsUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifacts_update_source_urls_error_component import (
        ApiV1ArtifactsUpdateSourceUrlsErrorComponent,
    )
    from ..models.api_v1_artifacts_update_spec_error_component import ApiV1ArtifactsUpdateSpecErrorComponent
    from ..models.api_v1_artifacts_update_target_availability_error_component import (
        ApiV1ArtifactsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifacts_update_version_error_component import ApiV1ArtifactsUpdateVersionErrorComponent
    from ..models.api_v1_artifacts_update_website_url_error_component import (
        ApiV1ArtifactsUpdateWebsiteUrlErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ArtifactsUpdateValidationError")


@_attrs_define
class ApiV1ArtifactsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ArtifactsUpdateActualAvailabilityErrorComponent |
            ApiV1ArtifactsUpdateAnnotationsErrorComponent | ApiV1ArtifactsUpdateAppVersionErrorComponent |
            ApiV1ArtifactsUpdateArchivedAtErrorComponent | ApiV1ArtifactsUpdateArchivedByErrorComponent |
            ApiV1ArtifactsUpdateArchivedErrorComponent | ApiV1ArtifactsUpdateArchivedReasonErrorComponent |
            ApiV1ArtifactsUpdateChangelogErrorComponent | ApiV1ArtifactsUpdateContentUrlErrorComponent |
            ApiV1ArtifactsUpdateCreatedByComponentErrorComponent | ApiV1ArtifactsUpdateCreatedByUserErrorComponent |
            ApiV1ArtifactsUpdateCriticalityErrorComponent | ApiV1ArtifactsUpdateDebugModeErrorComponent |
            ApiV1ArtifactsUpdateDefaultConfigErrorComponent | ApiV1ArtifactsUpdateDeprecatedErrorComponent |
            ApiV1ArtifactsUpdateDescriptionErrorComponent | ApiV1ArtifactsUpdateDigestErrorComponent |
            ApiV1ArtifactsUpdateDiscoveryEnabledErrorComponent | ApiV1ArtifactsUpdateDisplayNameErrorComponent |
            ApiV1ArtifactsUpdateKindErrorComponent | ApiV1ArtifactsUpdateLabelsErrorComponent |
            ApiV1ArtifactsUpdateLastReconciliationDurationSecondsErrorComponent | ApiV1ArtifactsUpdateLicenseErrorComponent
            | ApiV1ArtifactsUpdateManagedByContentTypeErrorComponent | ApiV1ArtifactsUpdateManagedByObjectIdErrorComponent |
            ApiV1ArtifactsUpdateMetadataErrorComponent | ApiV1ArtifactsUpdateMirroredAtErrorComponent |
            ApiV1ArtifactsUpdateMirroredContentUrlErrorComponent | ApiV1ArtifactsUpdateMirroredErrorComponent |
            ApiV1ArtifactsUpdateModifiedByUserErrorComponent | ApiV1ArtifactsUpdateNameErrorComponent |
            ApiV1ArtifactsUpdateNonFieldErrorsErrorComponent | ApiV1ArtifactsUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1ArtifactsUpdatePlatformServiceErrorComponent | ApiV1ArtifactsUpdatePrereleaseErrorComponent |
            ApiV1ArtifactsUpdateProviderErrorComponent | ApiV1ArtifactsUpdateProviderIdErrorComponent |
            ApiV1ArtifactsUpdateProviderReferenceErrorComponent | ApiV1ArtifactsUpdateReadmeMdErrorComponent |
            ApiV1ArtifactsUpdateReconciliationEnabledErrorComponent | ApiV1ArtifactsUpdateScopeErrorComponent |
            ApiV1ArtifactsUpdateSlaAvailabilityErrorComponent | ApiV1ArtifactsUpdateSlaTargetErrorComponent |
            ApiV1ArtifactsUpdateSlaWindowDaysErrorComponent | ApiV1ArtifactsUpdateSloAvailabilityErrorComponent |
            ApiV1ArtifactsUpdateSloTargetErrorComponent | ApiV1ArtifactsUpdateSloWindowDaysErrorComponent |
            ApiV1ArtifactsUpdateSourceUrlsErrorComponent | ApiV1ArtifactsUpdateSpecErrorComponent |
            ApiV1ArtifactsUpdateTargetAvailabilityErrorComponent | ApiV1ArtifactsUpdateVersionErrorComponent |
            ApiV1ArtifactsUpdateWebsiteUrlErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ArtifactsUpdateActualAvailabilityErrorComponent
        | ApiV1ArtifactsUpdateAnnotationsErrorComponent
        | ApiV1ArtifactsUpdateAppVersionErrorComponent
        | ApiV1ArtifactsUpdateArchivedAtErrorComponent
        | ApiV1ArtifactsUpdateArchivedByErrorComponent
        | ApiV1ArtifactsUpdateArchivedErrorComponent
        | ApiV1ArtifactsUpdateArchivedReasonErrorComponent
        | ApiV1ArtifactsUpdateChangelogErrorComponent
        | ApiV1ArtifactsUpdateContentUrlErrorComponent
        | ApiV1ArtifactsUpdateCreatedByComponentErrorComponent
        | ApiV1ArtifactsUpdateCreatedByUserErrorComponent
        | ApiV1ArtifactsUpdateCriticalityErrorComponent
        | ApiV1ArtifactsUpdateDebugModeErrorComponent
        | ApiV1ArtifactsUpdateDefaultConfigErrorComponent
        | ApiV1ArtifactsUpdateDeprecatedErrorComponent
        | ApiV1ArtifactsUpdateDescriptionErrorComponent
        | ApiV1ArtifactsUpdateDigestErrorComponent
        | ApiV1ArtifactsUpdateDiscoveryEnabledErrorComponent
        | ApiV1ArtifactsUpdateDisplayNameErrorComponent
        | ApiV1ArtifactsUpdateKindErrorComponent
        | ApiV1ArtifactsUpdateLabelsErrorComponent
        | ApiV1ArtifactsUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1ArtifactsUpdateLicenseErrorComponent
        | ApiV1ArtifactsUpdateManagedByContentTypeErrorComponent
        | ApiV1ArtifactsUpdateManagedByObjectIdErrorComponent
        | ApiV1ArtifactsUpdateMetadataErrorComponent
        | ApiV1ArtifactsUpdateMirroredAtErrorComponent
        | ApiV1ArtifactsUpdateMirroredContentUrlErrorComponent
        | ApiV1ArtifactsUpdateMirroredErrorComponent
        | ApiV1ArtifactsUpdateModifiedByUserErrorComponent
        | ApiV1ArtifactsUpdateNameErrorComponent
        | ApiV1ArtifactsUpdateNonFieldErrorsErrorComponent
        | ApiV1ArtifactsUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1ArtifactsUpdatePlatformServiceErrorComponent
        | ApiV1ArtifactsUpdatePrereleaseErrorComponent
        | ApiV1ArtifactsUpdateProviderErrorComponent
        | ApiV1ArtifactsUpdateProviderIdErrorComponent
        | ApiV1ArtifactsUpdateProviderReferenceErrorComponent
        | ApiV1ArtifactsUpdateReadmeMdErrorComponent
        | ApiV1ArtifactsUpdateReconciliationEnabledErrorComponent
        | ApiV1ArtifactsUpdateScopeErrorComponent
        | ApiV1ArtifactsUpdateSlaAvailabilityErrorComponent
        | ApiV1ArtifactsUpdateSlaTargetErrorComponent
        | ApiV1ArtifactsUpdateSlaWindowDaysErrorComponent
        | ApiV1ArtifactsUpdateSloAvailabilityErrorComponent
        | ApiV1ArtifactsUpdateSloTargetErrorComponent
        | ApiV1ArtifactsUpdateSloWindowDaysErrorComponent
        | ApiV1ArtifactsUpdateSourceUrlsErrorComponent
        | ApiV1ArtifactsUpdateSpecErrorComponent
        | ApiV1ArtifactsUpdateTargetAvailabilityErrorComponent
        | ApiV1ArtifactsUpdateVersionErrorComponent
        | ApiV1ArtifactsUpdateWebsiteUrlErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_artifacts_update_actual_availability_error_component import (
            ApiV1ArtifactsUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_update_annotations_error_component import (
            ApiV1ArtifactsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_artifacts_update_app_version_error_component import (
            ApiV1ArtifactsUpdateAppVersionErrorComponent,
        )
        from ..models.api_v1_artifacts_update_archived_at_error_component import (
            ApiV1ArtifactsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_artifacts_update_archived_by_error_component import (
            ApiV1ArtifactsUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_artifacts_update_archived_error_component import ApiV1ArtifactsUpdateArchivedErrorComponent
        from ..models.api_v1_artifacts_update_archived_reason_error_component import (
            ApiV1ArtifactsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_artifacts_update_changelog_error_component import (
            ApiV1ArtifactsUpdateChangelogErrorComponent,
        )
        from ..models.api_v1_artifacts_update_content_url_error_component import (
            ApiV1ArtifactsUpdateContentUrlErrorComponent,
        )
        from ..models.api_v1_artifacts_update_created_by_component_error_component import (
            ApiV1ArtifactsUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_artifacts_update_criticality_error_component import (
            ApiV1ArtifactsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_artifacts_update_debug_mode_error_component import (
            ApiV1ArtifactsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_artifacts_update_default_config_error_component import (
            ApiV1ArtifactsUpdateDefaultConfigErrorComponent,
        )
        from ..models.api_v1_artifacts_update_deprecated_error_component import (
            ApiV1ArtifactsUpdateDeprecatedErrorComponent,
        )
        from ..models.api_v1_artifacts_update_description_error_component import (
            ApiV1ArtifactsUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_artifacts_update_digest_error_component import ApiV1ArtifactsUpdateDigestErrorComponent
        from ..models.api_v1_artifacts_update_discovery_enabled_error_component import (
            ApiV1ArtifactsUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_artifacts_update_display_name_error_component import (
            ApiV1ArtifactsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_artifacts_update_kind_error_component import ApiV1ArtifactsUpdateKindErrorComponent
        from ..models.api_v1_artifacts_update_labels_error_component import ApiV1ArtifactsUpdateLabelsErrorComponent
        from ..models.api_v1_artifacts_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactsUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_artifacts_update_license_error_component import ApiV1ArtifactsUpdateLicenseErrorComponent
        from ..models.api_v1_artifacts_update_managed_by_content_type_error_component import (
            ApiV1ArtifactsUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_artifacts_update_managed_by_object_id_error_component import (
            ApiV1ArtifactsUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_artifacts_update_metadata_error_component import ApiV1ArtifactsUpdateMetadataErrorComponent
        from ..models.api_v1_artifacts_update_mirrored_at_error_component import (
            ApiV1ArtifactsUpdateMirroredAtErrorComponent,
        )
        from ..models.api_v1_artifacts_update_mirrored_content_url_error_component import (
            ApiV1ArtifactsUpdateMirroredContentUrlErrorComponent,
        )
        from ..models.api_v1_artifacts_update_mirrored_error_component import ApiV1ArtifactsUpdateMirroredErrorComponent
        from ..models.api_v1_artifacts_update_modified_by_user_error_component import (
            ApiV1ArtifactsUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_artifacts_update_name_error_component import ApiV1ArtifactsUpdateNameErrorComponent
        from ..models.api_v1_artifacts_update_non_field_errors_error_component import (
            ApiV1ArtifactsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_artifacts_update_platform_dns_record_created_error_component import (
            ApiV1ArtifactsUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_artifacts_update_platform_service_error_component import (
            ApiV1ArtifactsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_artifacts_update_prerelease_error_component import (
            ApiV1ArtifactsUpdatePrereleaseErrorComponent,
        )
        from ..models.api_v1_artifacts_update_provider_error_component import ApiV1ArtifactsUpdateProviderErrorComponent
        from ..models.api_v1_artifacts_update_provider_id_error_component import (
            ApiV1ArtifactsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_artifacts_update_provider_reference_error_component import (
            ApiV1ArtifactsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_artifacts_update_readme_md_error_component import (
            ApiV1ArtifactsUpdateReadmeMdErrorComponent,
        )
        from ..models.api_v1_artifacts_update_reconciliation_enabled_error_component import (
            ApiV1ArtifactsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_artifacts_update_scope_error_component import ApiV1ArtifactsUpdateScopeErrorComponent
        from ..models.api_v1_artifacts_update_sla_availability_error_component import (
            ApiV1ArtifactsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_update_sla_target_error_component import (
            ApiV1ArtifactsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_artifacts_update_sla_window_days_error_component import (
            ApiV1ArtifactsUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifacts_update_slo_availability_error_component import (
            ApiV1ArtifactsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_update_slo_target_error_component import (
            ApiV1ArtifactsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_artifacts_update_slo_window_days_error_component import (
            ApiV1ArtifactsUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifacts_update_source_urls_error_component import (
            ApiV1ArtifactsUpdateSourceUrlsErrorComponent,
        )
        from ..models.api_v1_artifacts_update_spec_error_component import ApiV1ArtifactsUpdateSpecErrorComponent
        from ..models.api_v1_artifacts_update_target_availability_error_component import (
            ApiV1ArtifactsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_update_version_error_component import ApiV1ArtifactsUpdateVersionErrorComponent
        from ..models.api_v1_artifacts_update_website_url_error_component import (
            ApiV1ArtifactsUpdateWebsiteUrlErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ArtifactsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateContentUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateWebsiteUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateSourceUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateAppVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateLicenseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateReadmeMdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateChangelogErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateDefaultConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateMirroredErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateMirroredContentUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateMirroredAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateDigestErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateDeprecatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdatePrereleaseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateMetadataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactsUpdateModifiedByUserErrorComponent):
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
        from ..models.api_v1_artifacts_update_actual_availability_error_component import (
            ApiV1ArtifactsUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_update_annotations_error_component import (
            ApiV1ArtifactsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_artifacts_update_app_version_error_component import (
            ApiV1ArtifactsUpdateAppVersionErrorComponent,
        )
        from ..models.api_v1_artifacts_update_archived_at_error_component import (
            ApiV1ArtifactsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_artifacts_update_archived_by_error_component import (
            ApiV1ArtifactsUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_artifacts_update_archived_error_component import ApiV1ArtifactsUpdateArchivedErrorComponent
        from ..models.api_v1_artifacts_update_archived_reason_error_component import (
            ApiV1ArtifactsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_artifacts_update_changelog_error_component import (
            ApiV1ArtifactsUpdateChangelogErrorComponent,
        )
        from ..models.api_v1_artifacts_update_content_url_error_component import (
            ApiV1ArtifactsUpdateContentUrlErrorComponent,
        )
        from ..models.api_v1_artifacts_update_created_by_component_error_component import (
            ApiV1ArtifactsUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_artifacts_update_created_by_user_error_component import (
            ApiV1ArtifactsUpdateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_artifacts_update_criticality_error_component import (
            ApiV1ArtifactsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_artifacts_update_debug_mode_error_component import (
            ApiV1ArtifactsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_artifacts_update_default_config_error_component import (
            ApiV1ArtifactsUpdateDefaultConfigErrorComponent,
        )
        from ..models.api_v1_artifacts_update_deprecated_error_component import (
            ApiV1ArtifactsUpdateDeprecatedErrorComponent,
        )
        from ..models.api_v1_artifacts_update_description_error_component import (
            ApiV1ArtifactsUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_artifacts_update_digest_error_component import ApiV1ArtifactsUpdateDigestErrorComponent
        from ..models.api_v1_artifacts_update_discovery_enabled_error_component import (
            ApiV1ArtifactsUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_artifacts_update_display_name_error_component import (
            ApiV1ArtifactsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_artifacts_update_kind_error_component import ApiV1ArtifactsUpdateKindErrorComponent
        from ..models.api_v1_artifacts_update_labels_error_component import ApiV1ArtifactsUpdateLabelsErrorComponent
        from ..models.api_v1_artifacts_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactsUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_artifacts_update_license_error_component import ApiV1ArtifactsUpdateLicenseErrorComponent
        from ..models.api_v1_artifacts_update_managed_by_content_type_error_component import (
            ApiV1ArtifactsUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_artifacts_update_managed_by_object_id_error_component import (
            ApiV1ArtifactsUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_artifacts_update_metadata_error_component import ApiV1ArtifactsUpdateMetadataErrorComponent
        from ..models.api_v1_artifacts_update_mirrored_at_error_component import (
            ApiV1ArtifactsUpdateMirroredAtErrorComponent,
        )
        from ..models.api_v1_artifacts_update_mirrored_content_url_error_component import (
            ApiV1ArtifactsUpdateMirroredContentUrlErrorComponent,
        )
        from ..models.api_v1_artifacts_update_mirrored_error_component import ApiV1ArtifactsUpdateMirroredErrorComponent
        from ..models.api_v1_artifacts_update_modified_by_user_error_component import (
            ApiV1ArtifactsUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_artifacts_update_name_error_component import ApiV1ArtifactsUpdateNameErrorComponent
        from ..models.api_v1_artifacts_update_non_field_errors_error_component import (
            ApiV1ArtifactsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_artifacts_update_platform_dns_record_created_error_component import (
            ApiV1ArtifactsUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_artifacts_update_platform_service_error_component import (
            ApiV1ArtifactsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_artifacts_update_prerelease_error_component import (
            ApiV1ArtifactsUpdatePrereleaseErrorComponent,
        )
        from ..models.api_v1_artifacts_update_provider_error_component import ApiV1ArtifactsUpdateProviderErrorComponent
        from ..models.api_v1_artifacts_update_provider_id_error_component import (
            ApiV1ArtifactsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_artifacts_update_provider_reference_error_component import (
            ApiV1ArtifactsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_artifacts_update_readme_md_error_component import (
            ApiV1ArtifactsUpdateReadmeMdErrorComponent,
        )
        from ..models.api_v1_artifacts_update_reconciliation_enabled_error_component import (
            ApiV1ArtifactsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_artifacts_update_scope_error_component import ApiV1ArtifactsUpdateScopeErrorComponent
        from ..models.api_v1_artifacts_update_sla_availability_error_component import (
            ApiV1ArtifactsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_update_sla_target_error_component import (
            ApiV1ArtifactsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_artifacts_update_sla_window_days_error_component import (
            ApiV1ArtifactsUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifacts_update_slo_availability_error_component import (
            ApiV1ArtifactsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_update_slo_target_error_component import (
            ApiV1ArtifactsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_artifacts_update_slo_window_days_error_component import (
            ApiV1ArtifactsUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifacts_update_source_urls_error_component import (
            ApiV1ArtifactsUpdateSourceUrlsErrorComponent,
        )
        from ..models.api_v1_artifacts_update_spec_error_component import ApiV1ArtifactsUpdateSpecErrorComponent
        from ..models.api_v1_artifacts_update_target_availability_error_component import (
            ApiV1ArtifactsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifacts_update_version_error_component import ApiV1ArtifactsUpdateVersionErrorComponent
        from ..models.api_v1_artifacts_update_website_url_error_component import (
            ApiV1ArtifactsUpdateWebsiteUrlErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ArtifactsUpdateActualAvailabilityErrorComponent
                | ApiV1ArtifactsUpdateAnnotationsErrorComponent
                | ApiV1ArtifactsUpdateAppVersionErrorComponent
                | ApiV1ArtifactsUpdateArchivedAtErrorComponent
                | ApiV1ArtifactsUpdateArchivedByErrorComponent
                | ApiV1ArtifactsUpdateArchivedErrorComponent
                | ApiV1ArtifactsUpdateArchivedReasonErrorComponent
                | ApiV1ArtifactsUpdateChangelogErrorComponent
                | ApiV1ArtifactsUpdateContentUrlErrorComponent
                | ApiV1ArtifactsUpdateCreatedByComponentErrorComponent
                | ApiV1ArtifactsUpdateCreatedByUserErrorComponent
                | ApiV1ArtifactsUpdateCriticalityErrorComponent
                | ApiV1ArtifactsUpdateDebugModeErrorComponent
                | ApiV1ArtifactsUpdateDefaultConfigErrorComponent
                | ApiV1ArtifactsUpdateDeprecatedErrorComponent
                | ApiV1ArtifactsUpdateDescriptionErrorComponent
                | ApiV1ArtifactsUpdateDigestErrorComponent
                | ApiV1ArtifactsUpdateDiscoveryEnabledErrorComponent
                | ApiV1ArtifactsUpdateDisplayNameErrorComponent
                | ApiV1ArtifactsUpdateKindErrorComponent
                | ApiV1ArtifactsUpdateLabelsErrorComponent
                | ApiV1ArtifactsUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1ArtifactsUpdateLicenseErrorComponent
                | ApiV1ArtifactsUpdateManagedByContentTypeErrorComponent
                | ApiV1ArtifactsUpdateManagedByObjectIdErrorComponent
                | ApiV1ArtifactsUpdateMetadataErrorComponent
                | ApiV1ArtifactsUpdateMirroredAtErrorComponent
                | ApiV1ArtifactsUpdateMirroredContentUrlErrorComponent
                | ApiV1ArtifactsUpdateMirroredErrorComponent
                | ApiV1ArtifactsUpdateModifiedByUserErrorComponent
                | ApiV1ArtifactsUpdateNameErrorComponent
                | ApiV1ArtifactsUpdateNonFieldErrorsErrorComponent
                | ApiV1ArtifactsUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1ArtifactsUpdatePlatformServiceErrorComponent
                | ApiV1ArtifactsUpdatePrereleaseErrorComponent
                | ApiV1ArtifactsUpdateProviderErrorComponent
                | ApiV1ArtifactsUpdateProviderIdErrorComponent
                | ApiV1ArtifactsUpdateProviderReferenceErrorComponent
                | ApiV1ArtifactsUpdateReadmeMdErrorComponent
                | ApiV1ArtifactsUpdateReconciliationEnabledErrorComponent
                | ApiV1ArtifactsUpdateScopeErrorComponent
                | ApiV1ArtifactsUpdateSlaAvailabilityErrorComponent
                | ApiV1ArtifactsUpdateSlaTargetErrorComponent
                | ApiV1ArtifactsUpdateSlaWindowDaysErrorComponent
                | ApiV1ArtifactsUpdateSloAvailabilityErrorComponent
                | ApiV1ArtifactsUpdateSloTargetErrorComponent
                | ApiV1ArtifactsUpdateSloWindowDaysErrorComponent
                | ApiV1ArtifactsUpdateSourceUrlsErrorComponent
                | ApiV1ArtifactsUpdateSpecErrorComponent
                | ApiV1ArtifactsUpdateTargetAvailabilityErrorComponent
                | ApiV1ArtifactsUpdateVersionErrorComponent
                | ApiV1ArtifactsUpdateWebsiteUrlErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_0 = (
                        ApiV1ArtifactsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_1 = (
                        ApiV1ArtifactsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_2 = (
                        ApiV1ArtifactsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_3 = (
                        ApiV1ArtifactsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_4 = (
                        ApiV1ArtifactsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_5 = (
                        ApiV1ArtifactsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_6 = (
                        ApiV1ArtifactsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_7 = (
                        ApiV1ArtifactsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_8 = (
                        ApiV1ArtifactsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_9 = (
                        ApiV1ArtifactsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_10 = (
                        ApiV1ArtifactsUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_11 = (
                        ApiV1ArtifactsUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_12 = (
                        ApiV1ArtifactsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_13 = (
                        ApiV1ArtifactsUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_14 = (
                        ApiV1ArtifactsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_15 = (
                        ApiV1ArtifactsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_16 = (
                        ApiV1ArtifactsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_17 = (
                        ApiV1ArtifactsUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_18 = (
                        ApiV1ArtifactsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_19 = (
                        ApiV1ArtifactsUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_20 = (
                        ApiV1ArtifactsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_21 = (
                        ApiV1ArtifactsUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_22 = (
                        ApiV1ArtifactsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_23 = (
                        ApiV1ArtifactsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_24 = (
                        ApiV1ArtifactsUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_25 = (
                        ApiV1ArtifactsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_26 = (
                        ApiV1ArtifactsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_27 = (
                        ApiV1ArtifactsUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_28 = (
                        ApiV1ArtifactsUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_29 = (
                        ApiV1ArtifactsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_30 = (
                        ApiV1ArtifactsUpdateContentUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_31 = (
                        ApiV1ArtifactsUpdateWebsiteUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_32 = (
                        ApiV1ArtifactsUpdateSourceUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_33 = (
                        ApiV1ArtifactsUpdateVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_34 = (
                        ApiV1ArtifactsUpdateAppVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_35 = (
                        ApiV1ArtifactsUpdateLicenseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_36 = (
                        ApiV1ArtifactsUpdateReadmeMdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_37 = (
                        ApiV1ArtifactsUpdateChangelogErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_38 = (
                        ApiV1ArtifactsUpdateSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_39 = (
                        ApiV1ArtifactsUpdateDefaultConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_40 = (
                        ApiV1ArtifactsUpdateMirroredErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_41 = (
                        ApiV1ArtifactsUpdateMirroredContentUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_42 = (
                        ApiV1ArtifactsUpdateMirroredAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_43 = (
                        ApiV1ArtifactsUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_44 = (
                        ApiV1ArtifactsUpdateDigestErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_45 = (
                        ApiV1ArtifactsUpdateDeprecatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_46 = (
                        ApiV1ArtifactsUpdatePrereleaseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_47 = (
                        ApiV1ArtifactsUpdateMetadataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_48 = (
                        ApiV1ArtifactsUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_49 = (
                        ApiV1ArtifactsUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifacts_update_error_type_50 = (
                        ApiV1ArtifactsUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifacts_update_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_artifacts_update_error_type_51 = (
                    ApiV1ArtifactsUpdateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_artifacts_update_error_type_51

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_artifacts_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_artifacts_update_validation_error.additional_properties = d
        return api_v1_artifacts_update_validation_error

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
