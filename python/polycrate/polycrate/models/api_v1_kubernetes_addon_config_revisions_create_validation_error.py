from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_addon_config_revisions_create_actual_availability_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_addon_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateAddonErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_annotations_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_archived_at_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_archived_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_archived_reason_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_block_config_template_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateBlockConfigTemplateErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_criticality_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_debug_mode_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_discovery_enabled_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_display_name_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_kind_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_labels_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_name_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_non_field_errors_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_platform_service_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_provider_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_provider_id_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_provider_reference_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_reconciliation_enabled_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_scope_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_sla_availability_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_sla_target_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_slo_availability_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_slo_target_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_target_availability_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_create_version_error_component import (
        ApiV1KubernetesAddonConfigRevisionsCreateVersionErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesAddonConfigRevisionsCreateValidationError")


@_attrs_define
class ApiV1KubernetesAddonConfigRevisionsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesAddonConfigRevisionsCreateActualAvailabilityErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateAddonErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateAnnotationsErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateArchivedAtErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateArchivedErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateArchivedReasonErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateBlockConfigTemplateErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateCriticalityErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateDebugModeErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateDisplayNameErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateKindErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateLabelsErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateNameErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateNonFieldErrorsErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreatePlatformServiceErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateProviderErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateProviderIdErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateProviderReferenceErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateReconciliationEnabledErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateScopeErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateSlaAvailabilityErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateSlaTargetErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateSloAvailabilityErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateSloTargetErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateTargetAvailabilityErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsCreateVersionErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesAddonConfigRevisionsCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateAddonErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateAnnotationsErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateArchivedAtErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateArchivedErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateArchivedReasonErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateBlockConfigTemplateErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateCriticalityErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateDebugModeErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateDisplayNameErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateKindErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateLabelsErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateNameErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreatePlatformServiceErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateProviderErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateProviderIdErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateProviderReferenceErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateScopeErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateSlaTargetErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateSloTargetErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateTargetAvailabilityErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsCreateVersionErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_addon_config_revisions_create_actual_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_addon_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateAddonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_annotations_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_archived_at_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_archived_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_archived_reason_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_criticality_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_debug_mode_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_discovery_enabled_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_display_name_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_kind_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_labels_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_name_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_non_field_errors_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_platform_service_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_provider_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_provider_id_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_provider_reference_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_scope_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_sla_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_sla_target_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_slo_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_slo_target_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_target_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_version_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateVersionErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateTargetAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateActualAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateAddonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsCreateVersionErrorComponent):
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
        from ..models.api_v1_kubernetes_addon_config_revisions_create_actual_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_addon_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateAddonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_annotations_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_archived_at_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_archived_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_archived_reason_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_block_config_template_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateBlockConfigTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_criticality_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_debug_mode_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_discovery_enabled_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_display_name_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_kind_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_labels_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_name_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_non_field_errors_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_platform_service_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_provider_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_provider_id_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_provider_reference_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_scope_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_sla_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_sla_target_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_slo_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_slo_target_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_target_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_create_version_error_component import (
            ApiV1KubernetesAddonConfigRevisionsCreateVersionErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesAddonConfigRevisionsCreateActualAvailabilityErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateAddonErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateAnnotationsErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateArchivedAtErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateArchivedErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateArchivedReasonErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateBlockConfigTemplateErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateCriticalityErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateDebugModeErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateDisplayNameErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateKindErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateLabelsErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateNameErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreatePlatformServiceErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateProviderErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateProviderIdErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateProviderReferenceErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateScopeErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateSlaTargetErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateSloTargetErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateTargetAvailabilityErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsCreateVersionErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_0 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_1 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_2 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_3 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_4 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_5 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_6 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_7 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_8 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_9 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_10 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_11 = (
                        ApiV1KubernetesAddonConfigRevisionsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_12 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_13 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_14 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_15 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_16 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_17 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_18 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_19 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_20 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_21 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_22 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_23 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_24 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateAddonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_25 = (
                        ApiV1KubernetesAddonConfigRevisionsCreateVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_26 = (
                    ApiV1KubernetesAddonConfigRevisionsCreateBlockConfigTemplateErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_addon_config_revisions_create_error_type_26

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_addon_config_revisions_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_addon_config_revisions_create_validation_error.additional_properties = d
        return api_v1_kubernetes_addon_config_revisions_create_validation_error

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
