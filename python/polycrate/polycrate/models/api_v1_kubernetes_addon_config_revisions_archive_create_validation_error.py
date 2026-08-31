from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_actual_availability_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_addon_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateAddonErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_annotations_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_archived_at_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_archived_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_archived_reason_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_block_config_template_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateBlockConfigTemplateErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_criticality_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_debug_mode_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_discovery_enabled_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_display_name_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_kind_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_labels_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_name_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_non_field_errors_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_platform_service_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_provider_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_provider_id_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_provider_reference_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_reconciliation_enabled_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_scope_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_sla_availability_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_sla_target_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_slo_availability_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_slo_target_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_target_availability_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_version_error_component import (
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateVersionErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesAddonConfigRevisionsArchiveCreateValidationError")


@_attrs_define
class ApiV1KubernetesAddonConfigRevisionsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesAddonConfigRevisionsArchiveCreateActualAvailabilityErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateAddonErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateAnnotationsErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedAtErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedReasonErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateBlockConfigTemplateErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateCriticalityErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateDebugModeErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateDisplayNameErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateKindErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateLabelsErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateNameErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreatePlatformServiceErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderIdErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderReferenceErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateScopeErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateSlaTargetErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateSloTargetErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateVersionErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesAddonConfigRevisionsArchiveCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateAddonErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateAnnotationsErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedAtErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedReasonErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateBlockConfigTemplateErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateCriticalityErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateDebugModeErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateDisplayNameErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateKindErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateLabelsErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateNameErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreatePlatformServiceErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderIdErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderReferenceErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateScopeErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateSlaTargetErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateSloTargetErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsArchiveCreateVersionErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_actual_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_addon_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateAddonErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_annotations_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_archived_at_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_archived_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_archived_reason_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_criticality_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_debug_mode_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_discovery_enabled_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_display_name_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_kind_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_labels_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_name_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_non_field_errors_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_platform_service_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_provider_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_provider_id_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_provider_reference_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_scope_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_sla_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_sla_target_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_slo_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_slo_target_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_target_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_version_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateVersionErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateNonFieldErrorsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateDisplayNameErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateAnnotationsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderReferenceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateDiscoveryEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreatePlatformServiceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedReasonErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateCriticalityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateTargetAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateActualAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateSloAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateSlaAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateAddonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsArchiveCreateVersionErrorComponent):
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
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_actual_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_addon_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateAddonErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_annotations_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_archived_at_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_archived_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_archived_reason_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_block_config_template_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateBlockConfigTemplateErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_criticality_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_debug_mode_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_discovery_enabled_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_display_name_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_kind_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_labels_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_name_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_non_field_errors_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_platform_service_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_provider_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_provider_id_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_provider_reference_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_scope_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_sla_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_sla_target_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_slo_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_slo_target_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_target_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_archive_create_version_error_component import (
            ApiV1KubernetesAddonConfigRevisionsArchiveCreateVersionErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesAddonConfigRevisionsArchiveCreateActualAvailabilityErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateAddonErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateAnnotationsErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedAtErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedReasonErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateBlockConfigTemplateErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateCriticalityErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateDebugModeErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateDisplayNameErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateKindErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateLabelsErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateNameErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreatePlatformServiceErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderIdErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderReferenceErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateScopeErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateSlaTargetErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateSloTargetErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsArchiveCreateVersionErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_0 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_1 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_2 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_3 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_4 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_5 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_6 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_7 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_8 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_9 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateReconciliationEnabledErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_10 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_11 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_12 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_13 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_14 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_15 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_16 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_17 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_18 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_19 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_20 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_21 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_22 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_23 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_24 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateAddonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_25 = (
                        ApiV1KubernetesAddonConfigRevisionsArchiveCreateVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_26 = (
                    ApiV1KubernetesAddonConfigRevisionsArchiveCreateBlockConfigTemplateErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_addon_config_revisions_archive_create_error_type_26

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_addon_config_revisions_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_addon_config_revisions_archive_create_validation_error.additional_properties = d
        return api_v1_kubernetes_addon_config_revisions_archive_create_validation_error

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
